from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self, p_type: str) -> None:
        self.p_type = p_type

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric")

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(x, (int, float))
                                              for x in data)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Numeric data invalid"
            c = len(data)
            s = sum(data)
            a = float(s) / c if c > 0 else 0.0
            return f"Processed {c} numeric values, sum={s}, avg={a}"
        except Exception as e:
            return f"Error: {e}"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Text data invalid"
            cnt = len(data)
            wrd = len(data.split())
            return f"Processed text: {cnt} characters, {wrd} words"
        except Exception as e:
            return f"Error: {e}"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Log entry invalid"
            parts = data.split(":", 1)
            lvl = parts[0]
            msg = parts[1].strip()
            tag = "ALERT" if lvl == "ERROR" else lvl
            return f"[{tag}] {lvl} level detected: {msg}"
        except Exception as e:
            return f"Error: {e}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    procs = [NumericProcessor(), TextProcessor(), LogProcessor()]
    d_list = [[1, 2, 3, 4, 5], "Hello Nexus World",
              "ERROR: Connection timeout"]
    v_msg = {"Numeric": "Numeric data verified",
             "Text": "Text data verified",
             "Log": "Log entry verified"}

    for p, d in zip(procs, d_list):
        print(f"Initializing {p.p_type} Processor...")
        if isinstance(d, str):
            print(f'Processing data: "{d}"')
        else:
            print(f"Processing data: {d}")
        if p.validate(d):
            print(f"Validation: {v_msg.get(p.p_type)}")
        print(p.format_output(p.process(d)))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    demo_d = [[1, 2, 3], "Hi Nexus", "INFO: System ready"]
    idx = 1
    for p, d in zip(procs, demo_d):
        print(f"Result {idx}: {p.process(d)}")
        idx += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
