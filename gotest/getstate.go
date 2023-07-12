package main

// TODO: Check if the respose is printed

import (
	"fmt"
	"net"

)

func main() {
	host := "192.168.1.158"
	port := 502
	data := []byte{0x00, 0x01, 0x00, 0x02, 0x00, 0x01, 0x0D}

	conn, err := net.Dial("tcp", fmt.Sprintf("%s:%d", host, port))
	if err != nil {
		fmt.Println("Error connecting to the server:", err)
		return
	}

	defer conn.Close()

	_, err = conn.Write(data)
	if err != nil {
		fmt.Println("Error sending data:", err)
		return
	}

	// Read response
	response := make([]byte, 1024)
	_, err = conn.Read(response)
	if err != nil {
		fmt.Println("Error reading response:", err)
		return
	}

	fmt.Println("Received response:", string(response))

	// Close the connection
	conn.Close()

	fmt.Println("Data sent and connection closed successfully.")
}

