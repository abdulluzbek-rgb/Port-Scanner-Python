# 🛡️ High-Speed Multi-Threaded Port Scanner

A professional-grade networking utility built with **Python** for rapid identification of open ports on a target host. This tool is engineered for efficiency, utilizing multi-threading and advanced queue management to perform network security audits and penetration testing tasks with high velocity.

## 🚀 Key Features

*   **Massive Concurrency:** Leverages **100 concurrent threads** to scan thousands of ports in a matter of seconds.
*   **Thread-Safe Queueing:** Implements a **FIFO Queue** to efficiently manage all 65,535 possible ports without data race conditions.
*   **Graceful Termination:** Fully supports `Ctrl + C` interruptions, ensuring the script exits cleanly without hanging.
*   **Optimized Performance:** Features balanced socket timeouts to maintain a high scanning speed while ensuring accurate detection of open ports.
*   **Low-Level Socket Interaction:** Utilizes the native Python `socket` library for direct communication with the TCP/IP stack.



## 🛠️ Technical Stack

*   **Language:** Python 3.x.
*   **Libraries:** 
    *   `socket`: For low-level network connectivity.
    *   `threading`: For executing asynchronous scanning tasks.
    *   `queue`: For synchronized task distribution among threads.

## 💻 How To Use

### 1. Installation
Clone the repository to your local environment:
```bash
git clone https://github.com/abdulluzbek-rgb/Port-Scanner-Python.git
cd Port-Scanner-Python
