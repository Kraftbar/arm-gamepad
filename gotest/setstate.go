package main

import (
	"encoding/hex"
	"fmt"
	"net"
	"time"
)

func main() {
	host := "192.168.1.158"
	port := 502
	data := []byte{0x00, 0x01,
				   0x00, 0x02, 
				   0x00, 0x03, 
				   0x0B, 
				   0x08, 
                   0x01}

	conn, err := net.DialTimeout("tcp", fmt.Sprintf("%s:%d", host, port), 5*time.Second) // 5 seconds timeout
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

	// Set a deadline for reading the response
	deadline := time.Now().Add(10 * time.Second) // Change the duration as per your requirement
	err = conn.SetReadDeadline(deadline)
	if err != nil {
		fmt.Println("Error setting read deadline:", err)
		return
	}

	// Read response
	response := make([]byte, 1024)
	n, err := conn.Read(response)
	if err != nil {
		if netErr, ok := err.(net.Error); ok && netErr.Timeout() {
			fmt.Println("Error reading response: Timeout")
		} else {
			fmt.Println("Error reading response:", err)
		}
		return
	}

	hexResponse := hex.EncodeToString(response[:n])
	fmt.Println("Response:", hexResponse)
	// Close the connection
	conn.Close()
}
