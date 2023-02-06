from typing import Optional

from openpyxl.worksheet.worksheet import Worksheet

from src.excel_generator.builder import AnalyticReportBuilder


class AnalyticTaskReportBuilder(AnalyticReportBuilder):
    """Строитель отчёта для заданий."""

    def __init__(self) -> None:
        self.sheet_name: str = "Задачи"
        self.header_data: tuple[str] = (
            "Задача",
            "Кол-во принятых отчётов",
            "Кол-во отклонённых отчётов",
            "Кол-во не предоставленных отчётов",
        )
        self.footer_data: tuple[str] = ("ИТОГО:", "=SUM(B2:B32)", "=SUM(C2:C32)", "=SUM(D2:D32)")
        self.worksheet: Optional[Worksheet] = None
        self.data_count: int = 0

    def add_footer(self) -> None:
        if self.data_count > 31:
            footer_data = [
                "ИТОГО:",
                f"=SUM(B2:B{self.data_count})",
                f"=SUM(C2:C{self.data_count})",
                f"=SUM(D2:D{self.data_count})",
            ]
            self.footer_data = tuple(footer_data)
        super().add_footer()
