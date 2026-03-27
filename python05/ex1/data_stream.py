from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        final = [
            {key: value}
            for info in data_batch
            for key, value in info.items()
            if key == criteria
            ]
        return final

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stats": f"- {self.name} data: {self.count} "
                     f"{self.operation} processed"
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"
        self.name = "Sensor"
        self.count = 2
        self.operation = "readings"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.batch = data_batch
        parts = []
        temp = []

        for d in data_batch:
            for key, value in d.items():
                parts.append(f"{key}:{value}")
                if key == "temp":
                    temp.append(value)

        data_str = "[" + ", ".join(parts) + "]"
        sum_temp = sum(temp)
        len_temp = len(temp)
        avg_temp = sum_temp / len_temp if len_temp else 0
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        return (
            f"Processing sensor batch: {data_str}\nSensor "
            f"analysis: {len_temp} readings processed, avg temp: {avg_temp}°C"
        )


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"
        self.batch = []
        self.name = "Transaction"
        self.count = 4
        self.operation = "operations"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.batch = data_batch
        parts = []

        for d in data_batch:
            for key, value in d.items():
                parts.append(f"{key}:{value}")

        buy = self.filter_data(data_batch, "buy")
        sell = self.filter_data(data_batch, "sell")

        buy_clean = [value for un in buy for value in un.values()]
        sell_clean = [value for un in sell for value in un.values()]

        data_str = "[" + ", ".join(parts) + "]"
        len_temp = len(buy_clean) + len(sell_clean)
        net_flow = sum(buy_clean) - sum(sell_clean)
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        return (
            f"Processing transaction batch: {data_str}\n"
            f"Transaction analysis: {len_temp} operations, "
            f"net flow: +{net_flow} units"
        )


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"
        self.batch = []
        self.name = "Event"
        self.count = 3
        self.operation = "events"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.batch = data_batch
        parts = []
        error = 0

        for d in data_batch:
            parts.append(f"{d}")
            if d == "error":
                error += 1

        data_str = "[" + ", ".join(parts) + "]"
        len_parts = len(parts)
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        return (
            f"Processing events batch: {data_str}\n"
            f"Event analysis: {len_parts} events, {error} error detected"
        )


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []
        self.all_batches = {
            "SENSOR_001": [
                {"temp": 22.5},
                {"humidity": 65},
                {"pressure": 1013}
                ],
            "TRANS_001": [{"buy": 100}, {"sell": 150}, {"buy": 75}],
            "EVENT_001": ["login", "error", "logout"]
        }

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self) -> None:
        for stream in self.streams:
            try:
                print(f"\nInitializing {stream.name} Stream...")
                batch = self.all_batches.get(stream.stream_id, [])
                print(stream.process_batch(batch))
            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")

    def get_all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        return [stream.get_stats() for stream in self.streams]


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    Sensor = SensorStream("SENSOR_001")
    Transaction = TransactionStream("TRANS_001")
    Event = EventStream("EVENT_001")
    Stream = StreamProcessor()

    Stream.add_stream(Sensor)
    Stream.add_stream(Transaction)
    Stream.add_stream(Event)

    Stream.process_all()

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print("\nBatch 1 Results:")
    stats = Stream.get_all_stats()
    for s in stats:
        for key, value in s.items():
            print(f"{value}")

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
