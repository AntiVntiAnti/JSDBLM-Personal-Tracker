from utility.logger_setup import create_logger
logger = create_logger(__name__)
from PyQt6.QtWidgets import QTextEdit, QFileDialog
from PyQt6.QtCore import QFileInfo, QByteArray
from PyQt6.QtGui import QTextDocument, QTextDocumentWriter
from PyQt6.QtPrintSupport import QPrinter



class TextEditSaver:
    """
    TextEditSaver is a class responsible for saving the content of a QTextEdit widget to a file. 
    It supports saving in various formats including PDF, text, markdown, and HTML.

    Methods:
        __init__():
            Initializes the TextEditSaver instance with no current QTextEdit widget set.

        set_current_text_edit(text_edit):

        save_current_text() -> None:
            Saves the current text in the text editor to a file.
    """
    def __init__(self):
        self.current_text_edit = None

    def set_current_text_edit(self, text_edit):
        """
        Sets the current text edit widget if the provided widget is an instance of QTextEdit.

        Args:
            text_edit (QTextEdit): The text edit widget to be set as the current text edit.

        Raises:
            Exception: If an error occurs during the process, it logs the error with the module name and exception details.
        """

        try:
            if isinstance(text_edit, QTextEdit):
                self.current_text_edit = text_edit
        except Exception as e:
            logger.error(f"Error in {__name__} {e}", exc_info=True)

    def save_current_text(self) -> None:
        """
        Saves the current text from the text editor to a file.

        The user is prompted with a file dialog to choose the location and name of the file.
        The file can be saved in one of the following formats: PDF, Text, Markdown, or HTML.
        If no valid extension is provided, the file is saved as a .txt file by default.

        Raises:
            Exception: If an error occurs during the file saving process, it is logged.

        Returns:
            None
        """

        try:
            if self.current_text_edit is None:
                return

            options = "PDF Files (*.pdf);;Text Files (*.txt);;Markdown Files (*.md);;HTML Files (*.html)"
            filename, _ = QFileDialog.getSaveFileName(None, "Save File", "", options)

            if filename:
                file_extension = QFileInfo(filename).suffix().lower()

                if file_extension not in ["txt", "md", "html", "pdf"]:
                    filename += ".txt"  # Default to .txt if no valid extension is provided

                if file_extension == "pdf":
                    printer = QPrinter(QPrinter.PrinterMode.HighResolution)
                    printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                    printer.setOutputFileName(filename)
                    self.current_text_edit.document().print(printer)
                else:
                    with open(filename, 'w', encoding='utf-REFACTOR NOTES 8-30') as file:
                        if file_extension == "html":
                            file.write(self.current_text_edit.toHtml())
                        elif file_extension == "txt":
                            file.write(self.current_text_edit.toPlainText())
                        elif file_extension == "md":
                            file.write(self.current_text_edit.toMarkdown())
                logger.info(f"Saved file: {filename}, Extension: {file_extension}")
            else:
                logger.info("File not saved")
        except Exception as e:
            logger.error(f"Error in {__name__} {e}", exc_info=True)
