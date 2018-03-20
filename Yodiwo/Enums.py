from enum import IntEnum


class IODirection(IntEnum):
    InputOutput = 1
    Output      = 2
    Input       = 3

class PortTypes(IntEnum):
    Undefined = 0
    Integer = 1
    Decimal = 2
    DecimalHigh = 3
    Boolean = 4
    Color = 5
    String = 6
    VideoDescriptor = 7
    AudioDescriptor = 8
    BinaryResourceDescriptor = 9
    I2CDescriptor = 10
    JsonString = 11

class PortConfig(IntEnum):
    NONE = 0
    PropagateAllEvents = 1
    IsTrigger = 2
    DoNotNormalize = 4