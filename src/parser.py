import pdfplumber
import re


def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = _extract_page_text(page)
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""
    return clean_text(text)


def _extract_page_text(page):
    """
    Tries multiple extraction strategies in order:
    1. Word-level line grouping (most reliable for all layouts)
    2. Column-aware extraction (two-column resumes)
    3. Standard extract_text (simple single-column PDFs)
    """

    # Strategy 1: Word-level extraction grouped by vertical position
    # This is the most reliable strategy — handles single column,
    # two-column, and mixed layouts correctly
    try:
        words = page.extract_words(
            x_tolerance=3,
            y_tolerance=3,
            keep_blank_chars=False
        )
        if words and len(words) > 5:
            lines = {}
            for word in words:
                line_key = round(word['top'])
                if line_key not in lines:
                    lines[line_key] = []
                lines[line_key].append((word['x0'], word['text']))

            result_lines = []
            for key in sorted(lines.keys()):
                line_words = sorted(lines[key], key=lambda x: x[0])
                line_text = " ".join(w[1] for w in line_words)
                result_lines.append(line_text)

            result = "\n".join(result_lines)
            if len(result.strip()) > 80:
                return result
    except Exception:
        pass

    # Strategy 2: Column-aware extraction for two-column layouts
    try:
        width = page.width
        height = page.height

        left_bbox  = (0, 0, width * 0.48, height)
        right_bbox = (width * 0.48, 0, width, height)

        left_page  = page.crop(left_bbox)
        right_page = page.crop(right_bbox)

        left_text  = left_page.extract_text(x_tolerance=3, y_tolerance=3) or ""
        right_text = right_page.extract_text(x_tolerance=3, y_tolerance=3) or ""

        combined = (left_text + "\n" + right_text).strip()
        if len(combined) > 80:
            return combined
    except Exception:
        pass

    # Strategy 3: Standard extraction fallback
    try:
        standard_text = page.extract_text(x_tolerance=3, y_tolerance=3)
        if standard_text and len(standard_text.strip()) > 10:
            return standard_text
    except Exception:
        pass

    return ""


def clean_text(text):
    # Step 1: Remove PDF encoding artifacts
    text = re.sub(r'\(cid:\d+\)', ' ', text)

    # Step 2: Remove non-ASCII characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    # Step 3: Clean each line individually — preserve newlines
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # Collapse multiple spaces within a line
        line = re.sub(r'[ \t]+', ' ', line).strip()
        if line:
            cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)


def extract_text_from_string(text):
    return clean_text(text)