from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QPainterPath, QRegion, QMouseEvent, QResizeEvent
from utility.logger_setup import create_logger
logger = create_logger(__name__)


class FramelessDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.startPos = None
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.pressing = False

    def mousePressEvent(self, event: QMouseEvent) -> None:
        try:
            if event.button() == Qt.MouseButton.LeftButton:
                self.pressing = True
                self.startPos = event.position().toPoint()
        except Exception as e:
            logger.error(f"Error in mousePressEvent: {e}", exc_info=True)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        try:
            if self.pressing and self.startPos is not None:
                self.move(self.pos() + event.position().toPoint() - self.startPos)
        except Exception as e:
            logger.error(f"Error in mouseMoveEvent: {e}", exc_info=True)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        try:
            if event.button() == Qt.MouseButton.LeftButton:
                self.pressing = False
        except Exception as e:
            logger.error(f"error occurred mouseReleaseEvent: {e}", exc_info=True)

    def resizeEvent(self, event: QResizeEvent):
        try:
            path = QPainterPath()
            path.addRoundedRect(QRectF(self.rect()), 10.0, 10.0)

            region = QRegion(path.toFillPolygon().toPolygon())
            self.setMask(region)
        except Exception as e:
            logger.error(f"Error in resizeEvent: {e}", exc_info=True)
