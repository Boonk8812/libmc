// Import necessary packages
import com.fazecast.jserialcomm.*

const val PORT_NAME = "/dev/ttyUSB0"; // Specify your serial device name here
val SERIAL_PORT = SerialPort(PORT_NAME, 9600)

fun main() {
    initSerialConnection()

    /* Perform your serial operations here */
    SERIAL_PORT.outputStream?.writer()?.use { writer ->
        writer.println("Hello, Raspberry Pi!")
    }

    closeSerialConnection()
}

private fun initSerialConnection() {
    if (!SERIAL_PORT.isOpen) {
        SERIAL_PORT.openPort()
        SERIAL_PORT.setComPortParameters(9600, 8, SerialPort.ONE_STOP_BIT, SerialPort.NO_PARITY)
    }
}

private fun closeSerialConnection() {
    SERIAL_PORT.closePort()
}
