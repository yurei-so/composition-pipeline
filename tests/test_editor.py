import unittest

from composition_pipeline import EditProtocolError, apply_edit_document


class EditorProtocolTest(unittest.TestCase):
    def test_applies_append_replace_delete_and_finalize(self) -> None:
        result, edits = apply_edit_document({"operations": [
            {"op": "append", "text": "The quick brown fox is very ready."},
            {"op": "replace", "old": "very ready", "new": "ready"},
            {"op": "delete", "text": "quick "},
            {"op": "finalize"},
        ]})
        self.assertEqual(result, "The brown fox is ready.")
        self.assertEqual(edits, 2)

    def test_rejects_ambiguous_replace(self) -> None:
        with self.assertRaisesRegex(EditProtocolError, "exactly once"):
            apply_edit_document({"operations": [
                {"op": "append", "text": "same same"},
                {"op": "replace", "old": "same", "new": "different"},
                {"op": "finalize"},
            ]})

    def test_rejects_operations_after_finalize(self) -> None:
        with self.assertRaisesRegex(EditProtocolError, "finalize"):
            apply_edit_document({"operations": [
                {"op": "append", "text": "done"},
                {"op": "finalize"},
                {"op": "append", "text": "not done"},
            ]})
