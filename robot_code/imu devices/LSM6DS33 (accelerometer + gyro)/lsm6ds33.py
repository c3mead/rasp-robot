class LSM6DS33():
    """ """
    def __init__(self):
        self.addr = 0x6b
    # Register addresses - reserved addresses removed
    
    LSM_FUNC_CFG_ACCESS   = 0x01  
    
    LSM_FIFO_CTRL1        = 0x06
    LSM_FIFO_CTRL2        = 0x07
    LSM_FIFO_CTRL3        = 0x08
    LSM_FIFO_CTRL4        = 0x09
    LSM_FIFO_CTRL5        = 0x0A

    LSM_ORIENT_CFG_G      = 0x0B

    LSM_INT1_CTRL         = 0x0D
    LSM_INT2_CTRL         = 0x0E
    LSM_WHO_AM_I          = 0x0F
    LSM_CTRL1_XL          = 0x10
    LSM_CTRL2_G           = 0x11
    LSM_CTRL3_C           = 0x12
    LSM_CTRL4_C           = 0x13
    LSM_CTRL5_C           = 0x14
    LSM_CTRL6_C           = 0x15
    LSM_CTRL7_G           = 0x16
    LSM_CTRL8_XL          = 0x17
    LSM_CTRL9_XL          = 0x18
    LSM_CTRL10_C          = 0x19

    LSM_WAKE_UP_SRC       = 0x1B
    LSM_TAP_SRC           = 0x1C
    LSM_D6D_SRC           = 0x1D

    LSM_STATUS_REG        = 0x1E

    LSM_OUT_TEMP_L        = 0x20  # Temperature output, low byte
    LSM_OUT_TEMP_H        = 0x21  # Temperature output, high byte
    LSM_OUTX_L_G          = 0x22  # Gyroscope X output, low byte
    LSM_OUTX_H_G          = 0x23  # Gyroscope X output, high byte
    LSM_OUTY_L_G          = 0x24  # Gyroscope Y output, low byte
    LSM_OUTY_H_G          = 0x25  # Gyroscope Y output, high byte
    LSM_OUTZ_L_G          = 0x26  # Gyroscope Z output, low byte
    LSM_OUTZ_H_G          = 0x27  # Gyroscope Z output, high byte
    LSM_OUTX_L_XL         = 0x28  # Accelerometer X output, low byte
    LSM_OUTX_H_XL         = 0x29  # Accelerometer X output, high byte
    LSM_OUTY_L_XL         = 0x2A  # Accelerometer Y output, low byte
    LSM_OUTY_H_XL         = 0x2B  # Accelerometer Y output, high byte
    LSM_OUTZ_L_XL         = 0x2C  # Accelerometer Z output, low byte
    LSM_OUTZ_H_XL         = 0x2D  # Accelerometer Z output, high byte

    LSM_FIFO_STATUS1      = 0x3A
    LSM_FIFO_STATUS2      = 0x3B
    LSM_FIFO_STATUS3      = 0x3C
    LSM_FIFO_STATUS4      = 0x3D
    LSM_FIFO_DATA_OUT_L   = 0x3E
    LSM_FIFO_DATA_OUT_H   = 0x3F

    LSM_TIMESTAMP0_REG    = 0x40
    LSM_TIMESTAMP1_REG    = 0x41
    LSM_TIMESTAMP2_REG    = 0x42

    LSM_STEP_TIMESTAMP_L  = 0x49
    LSM_STEP_TIMESTAMP_H  = 0x4A
    LSM_STEP_COUNTER_L    = 0x4B
    LSM_STEP_COUNTER_H    = 0x4C

    LSM_FUNC_SRC          = 0x53

    LSM_TAP_CFG           = 0x58
    LSM_TAP_THS_6D        = 0x59
    LSM_INT_DUR2          = 0x5A
    LSM_WAKE_UP_THS       = 0x5B
    LSM_WAKE_UP_DUR       = 0x5C
    LSM_FREE_FALL         = 0x5D
    LSM_MD1_CFG           = 0x5E
    LSM_MD2_CFG           = 0x5F

# Output registers used by the accelerometer
    accl_regs = [
        LSM_OUTX_L_XL,       # low byte of X value
        LSM_OUTX_H_XL,       # high byte of X value
        LSM_OUTY_L_XL,       # low byte of Y value
        LSM_OUTY_H_XL,       # high byte of Y value
        LSM_OUTZ_L_XL,       # low byte of Z value
        LSM_OUTZ_H_XL,       # high byte of Z value
    ]

# Output registers used by the gyroscope
    gyro_regs = [
        LSM_OUTX_L_G,       # low byte of X value
        LSM_OUTX_H_G,       # high byte of X value
        LSM_OUTY_L_G,       # low byte of Y value
        LSM_OUTY_H_G,       # high byte of Y value
        LSM_OUTZ_L_G,       # low byte of Z value
        LSM_OUTZ_H_G,       # high byte of Z value
    ]

# Output registers used by the temperature sensor
    temp_regs = [
        LSM_OUT_TEMP_L,     # low byte of temperature value
        LSM_OUT_TEMP_H,     # high byte of temperature value
    ]
