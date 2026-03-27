from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, list):
                return False
            for x in data:
                if not isinstance(x, (int, float)):
                    return False
            return True
        except Exception:
            return False

    def format_output(self, result: list) -> str:
        res_size = len(result)
        res_sum = 0
        for val in result:
            res_sum += val
        res_avg = res_sum / res_size if res_size > 0 else 0.0
        return (f"Processed {res_size} numeric values, "
                f"sum={res_sum}, avg={res_avg}")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        return f'Processing data: "{data}"'

    def validate(self, data: Any) -> bool:
        try:
            return isinstance(data, str)
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        res_char = len(result)
        res_word = len(result.split())
        return f"Processed text: {res_char} characters, {res_word} words"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        try:
            return isinstance(data, str) and "ERROR" in data
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return "[ALERT] ERROR level detected:"


def main() -> None:
    num_p = NumericProcessor()
    txt_p = TextProcessor()
    log_p = LogProcessor()

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    d1 = [1, 2, 3, 4, 5]
    print("\nInitializing Numeric Processor...")
    print(num_p.process(d1))
    if num_p.validate(d1):
        print("Validation: Numeric data verified")
        print("Output:", num_p.format_output(d1))

    d2 = "Hello Nexus World"
    print("\nInitializing Text Processor...")
    print(txt_p.process(d2))
    if txt_p.validate(d2):
        print("Validation: Text data verified")
        print("Output:", txt_p.format_output(d2))

    d3 = "ERROR: Connection timeout"
    d3_m = "ERROR level detected: Connection timeout"
    print("\nInitializing Log Processor...")
    print(log_p.process(d3))
    if log_p.validate(d3):
        print("Validation: Log entry verified")
        print("Output:", log_p.format_output(d3_m), "Connection timeout")

    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")
    print(f"Result 1: {num_p.format_output(d1)}")
    print(f"Result 2: {txt_p.format_output(d2)}")
    print(f"Result 3: {log_p.format_output(d3)} System ready")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
