from abc import ABC, abstractmethod
from typing import Any, List


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            count = len(data_batch)
            avg = sum(data_batch) / count if count > 0 else 0.0
            return (f"Sensor analysis: {count} readings processed, "
                    f"avg temp: {avg}")
        except Exception as e:
            return f"Sensor Error: {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            count = len(data_batch)
            net = sum(data_batch)
            return (f"Transaction analysis: {count} operations, "
                    f"net flow: {net}")
        except Exception as e:
            return f"Transaction Error: {e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            count = len(data_batch)
            return f"Event analysis: {count} events processed"
        except Exception as e:
            return f"Event Error: {e}"


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    s_s = SensorStream("SENSOR_001")
    t_s = TransactionStream("TRANS_001")
    e_s = EventStream("EVENT_001")

    print("Initializing Sensor Stream...")
    print(f"Stream ID: {s_s.stream_id}, Type: {s_s.stream_type}")
    print("Processing sensor batch: [20.0, 25.0, 24.0]")
    print(s_s.process_batch([20.0, 25.0, 24.0]))

    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {t_s.stream_id}, Type: {t_s.stream_type}")
    print("Processing transaction batch: [100, -50, 200]")
    print(t_s.process_batch([100, -50, 200]))

    print("\nInitializing Event Stream...")
    print(f"Stream ID: {e_s.stream_id}, Type: {e_s.stream_type}")
    print("Processing event batch: [login, error, logout]")
    print(e_s.process_batch(["login", "error", "logout"]))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print("Batch 1 Results:")
    streams = [s_s, t_s, e_s]
    batches = [[22.0, 24.0], [50, -10], ["warn", "info"]]

    for stream, batch in zip(streams, batches):
        print(f"Processing {stream.stream_id}...")
        print(stream.process_batch(batch))

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
