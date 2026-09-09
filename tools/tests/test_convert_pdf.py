"""Tests for tools/convert_pdf_interfaces.py (standard library unittest only)."""
import tempfile
import unittest
from pathlib import Path

from tools.convert_pdf_interfaces import (
    ITEM_RE,
    chapter_dirname,
    existing_chapter_dirs,
    join_same_row,
    parse_release_history,
    render_function,
    sanitize_filename,
    slugify,
)


class JoinSameRowTests(unittest.TestCase):
    def test_single_row_join_with_gap_spaces(self):
        rows = join_same_row([
            {"y": 457.0, "x0": 72.5, "x1": 94.0, "text": "DLL: "},
            {"y": 457.0, "x0": 104.5, "x1": 155.0, "text": "tcextcomapi "},
        ])
        self.assertEqual(rows, ["DLL:   tcextcomapi"])

    def test_separate_rows_stay_separate(self):
        rows = join_same_row([
            {"y": 457.0, "x0": 72.5, "x1": 94.0, "text": "DLL: "},
            {"y": 476.6, "x0": 104.5, "x1": 318.8, "text": "This function is available. "},
        ])
        self.assertEqual(rows, ["DLL:", "This function is available."])

    def test_body_lines_lstripped_like_legacy(self):
        rows = join_same_row([
            {"y": 505.7, "x0": 109.3, "x1": 383.0,
             "text": "               domain  tccadr.nama      iAddressName mb, "},
        ])
        self.assertEqual(rows, ["domain  tccadr.nama      iAddressName mb,"])


class RenderFunctionTests(unittest.TestCase):
    def test_rows_never_merge_across_pages(self):
        md = render_function({
            "name": "Address.Create",
            "chapter_num": 3,
            "chapter": "Chapter 3 Public Interfaces for Common",
            "group": "Public Interfaces for Address",
            "pages": [86, 87],
            "printed": [87, 88],
            "linelets": [
                {"y": 91.8, "x0": 109.3, "x1": 392.6,
                 "text": "boolean          iSetBuildingFloor,", "page": 86},
                {"y": 91.8, "x0": 109.3, "x1": 378.2,
                 "text": "iAddressLine5           - Address Line 5", "page": 87},
            ],
        })
        self.assertIn("boolean          iSetBuildingFloor,\n", md)
        self.assertIn("iAddressLine5           - Address Line 5\n", md)
        self.assertNotIn("iSetBuildingFloor, iAddressLine5", md)

    def test_blockquote_and_fence(self):
        md = render_function({
            "name": "X.Y", "chapter_num": 3, "chapter": "Chapter 3 C",
            "group": "G", "pages": [1], "printed": [86, 88], "linelets": [],
        })
        self.assertTrue(md.startswith("# X.Y\n"))
        self.assertIn("> Chapter: Chapter 3 C", md)
        self.assertIn("> Group: G", md)
        self.assertIn("pp. 86-88", md)
        self.assertIn("```baan", md)


class FilenameTests(unittest.TestCase):
    def test_dotted_name_unchanged(self):
        self.assertEqual(sanitize_filename("Address.Create"), "Address.Create")
        self.assertEqual(sanitize_filename("whext.dll0019.freeze.confirm.shipment.line.handle.before.check"),
                         "whext.dll0019.freeze.confirm.shipment.line.handle.before.check")

    def test_invalid_chars_replaced(self):
        self.assertEqual(sanitize_filename("A/B:C"), "A_B_C")

    def test_slugify(self):
        self.assertEqual(slugify("Public Interfaces for Common"), "public_interfaces_for_common")

    def test_chapter_dirname_reuses_existing(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            (out / "ch03_common").mkdir()
            mapping = existing_chapter_dirs(out)
            self.assertEqual(mapping, {3: "ch03_common"})
            self.assertEqual(chapter_dirname(3, "Chapter 3 Public Interfaces for Common", mapping),
                             "ch03_common")
            # Canonical slug table applies even without an existing dir.
            self.assertEqual(chapter_dirname(4, "Chapter 4 Public Interfaces for Calendar", {}),
                             "ch04_calendar")
            # Unknown chapters fall back to slugified titles.
            self.assertEqual(chapter_dirname(99, "Chapter 99 Brand New Topic", {}),
                             "ch99_brand_new_topic")


class ReleaseHistoryTests(unittest.TestCase):
    LINES = [
        "Public Interfaces and Process Extensions per Infor LN Cloud release ",
        "2361 | Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud) ",
        "Appendix A Public Interfaces and Process ",
        "Extensions per Infor LN Cloud release ",
        "Public Interfaces ",
        "The following table shows the Infor LN Cloud releases in which new Public Interfaces were released: ",
        "Release Public Interface ",
        "2019.01 BOD.ExecuteMethod ",
        "BOD.Publish ",
        "2026.07 Call.SetStatusToInProcess ",
        "OutboundAdvice.Pick ",
        "2026.08 Call.CreateInvoice ",
        "EngineeringItem.GenerateByMBC ",
        "Process Extensions ",
        "The following table shows the Infor LN Cloud releases in which new Process Extensions were released: ",
        "Release Process Extension ",
        "2019.07 PurchaseSelfBilledInvoice.CustomCompose ",
        "2026.08 SomeNew.SkipSomething ",
    ]

    def test_parse(self):
        title, ifaces, exts = parse_release_history(self.LINES)
        self.assertIn("Appendix A", " ".join(title))
        self.assertEqual([r for r, _ in ifaces], ["2019.01", "2026.07", "2026.08"])
        self.assertEqual(ifaces[0][1], ["BOD.ExecuteMethod", "BOD.Publish"])
        self.assertEqual(ifaces[2][1], ["Call.CreateInvoice", "EngineeringItem.GenerateByMBC"])
        self.assertEqual(exts[0], ("2019.07", ["PurchaseSelfBilledInvoice.CustomCompose"]))
        self.assertEqual(exts[1], ("2026.08", ["SomeNew.SkipSomething"]))

    def test_item_pattern(self):
        self.assertTrue(ITEM_RE.match("Address.Create"))
        self.assertTrue(ITEM_RE.match("ciext.sli0005.split.revenue.by.component"))
        self.assertFalse(ITEM_RE.match("Release Public Interface"))
        self.assertFalse(ITEM_RE.match("The following table shows"))


class PdfSmokeTests(unittest.TestCase):
    @unittest.skipUnless(__import__("glob").glob("update/*.pdf"),
                         "requires source PDF in update/")
    def test_guide_pdf_present_and_sized(self):
        import glob
        pdfs = glob.glob("update/*.pdf")
        self.assertEqual(len(pdfs), 1)
        import pymupdf
        doc = pymupdf.open(pdfs[0])
        try:
            self.assertEqual(doc.page_count, 2361)
            self.assertIn("25082026", pdfs[0])
        finally:
            doc.close()


if __name__ == "__main__":
    unittest.main()
