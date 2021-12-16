from __future__ import annotations
from dataclasses import dataclass
import operator
from bitstring import BitStream, BitArray
from functools import reduce


def read_bits():
    with open('data/day16') as f:
        bits = BitStream(hex(int(f.read().strip(), 16)))
    return bits


@dataclass
class BitPacket:
    version: int
    type_id: int


@dataclass
class BitLiteral(BitPacket):
    literal: int

    @classmethod
    def parse_literal(cls, version: int, type_id: int, stream: BitStream) -> BitLiteral:
        lit = BitArray()
        cont_flag = True
        while cont_flag:
            cont_flag = stream.read(1)
            lit.append(stream.read(4))

        return cls(version, type_id, lit.uint)

    def version_sum(self) -> int:
        return self.version

    def value(self) -> int:
        return self.literal


@dataclass
class BitOperator(BitPacket):
    packets: list[BitPacket]

    @classmethod
    def parse_operator(cls, version: int, type_id: int, stream: BitStream) -> BitOperator:
        if stream.read('bool'):
            length = stream.read('uint:11')
            packets = [parse_packet(stream) for _ in range(length)]

        else:
            length = stream.read('uint:15')
            endpos = stream.pos + length
            packets = []
            while stream.pos < endpos:
                pkt = parse_packet(stream)
                packets.append(pkt)

        return cls(version, type_id, packets)

    def version_sum(self) -> int:
        return self.version + sum(pkt.version_sum() for pkt in self.packets)

    def value(self) -> int:
        values = (pkt.value() for pkt in self.packets)
        match self.type_id:
            case 0:
                return sum(values)
            case 1:
                return reduce(operator.__mul__, values)
            case 2:
                return min(values)
            case 3:
                return max(values)
            case 5:
                return operator.gt(*values)
            case 6:
                return operator.lt(*values)
            case 7:
                return operator.eq(*values)


def parse_packet(stream: BitStream) -> BitPacket:
    version = stream.read('uint:3')
    type_id = stream.read('uint:3')
    if type_id == 4:
        ret = BitLiteral.parse_literal(version, type_id, stream)
    else:
        ret = BitOperator.parse_operator(version, type_id, stream)

    return ret


def one():
    '''Part One'''
    stream = read_bits()
    pkt = parse_packet(stream)
    return pkt.version_sum()


def two():
    '''Part Two'''
    stream = read_bits()
    pkt = parse_packet(stream)
    return pkt.value()


def main() -> None:
    print(one())
    print(two())


if __name__ == '__main__':
    main()
