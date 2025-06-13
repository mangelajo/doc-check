Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode

Hide navigation sidebar

Hide table of contents sidebar

[Skip to content](#furo-main-content)

Toggle site navigation sidebar

[jumpstarter](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

[![Logo](_static/logo-light-theme.svg)](#)

- [Introduction](#document-introduction/index)
  
  Toggle navigation of Introduction
  
  - [Drivers](#document-introduction/drivers)
  - [Adapters](#document-introduction/adapters)
  - [Exporters](#document-introduction/exporters)
  - [Clients](#document-introduction/clients)
  - [Service](#document-introduction/service)
- [Getting Started](#document-getting-started/index)
  
  Toggle navigation of Getting Started
  
  - [Installation](#document-getting-started/installation/index)
    
    Toggle navigation of Installation
    
    - [Packages](#document-getting-started/installation/packages)
    - [Service](#document-getting-started/installation/service)
  - [Configuration](#document-getting-started/configuration/index)
    
    Toggle navigation of Configuration
    
    - [Files](#document-getting-started/configuration/files)
    - [Loading Order](#document-getting-started/configuration/loading-order)
    - [Authentication](#document-getting-started/configuration/authentication)
  - [Usage](#document-getting-started/usage/index)
    
    Toggle navigation of Usage
    
    - [Setup Local Mode](#document-getting-started/usage/setup-local-mode)
    - [Setup Distributed Mode](#document-getting-started/usage/setup-distributed-mode)
    - [Examples](#document-getting-started/usage/examples)
    - [Integration Patterns](#document-getting-started/usage/integration-patterns)
- [Contributing](#document-contributing)
  
  Toggle navigation of Contributing
  
  - [Development Environment](#document-contributing/development-environment)
  - [Internals](#document-contributing/internals)
- [Glossary](#document-glossary)
- [Reference](#document-reference/index)
  
  Toggle navigation of Reference
  
  - [MAN Pages](#document-reference/man-pages/index)
    
    Toggle navigation of MAN Pages
    
    - [jmp](#document-reference/man-pages/jmp)
    - [j](#document-reference/man-pages/j)
  - [Package APIs](#document-reference/package-apis/index)
    
    Toggle navigation of Package APIs
    
    - [Driver Packages](#document-reference/package-apis/drivers/index)
      
      Toggle navigation of Driver Packages
      
      - [CAN driver](#document-reference/package-apis/drivers/can)
      - [Corellium Driver](#document-reference/package-apis/drivers/corellium)
      - [DUT Link driver](#document-reference/package-apis/drivers/dutlink)
      - [EnerGenie](#document-reference/package-apis/drivers/energenie)
      - [Flashers](#document-reference/package-apis/drivers/flashers)
      - [HTTP driver](#document-reference/package-apis/drivers/http)
      - [Network drivers](#document-reference/package-apis/drivers/network)
      - [OpenDAL driver](#document-reference/package-apis/drivers/opendal)
      - [Power driver](#document-reference/package-apis/drivers/power)
      - [probe-rs driver](#document-reference/package-apis/drivers/probe-rs)
      - [PySerial driver](#document-reference/package-apis/drivers/pyserial)
      - [QEMU driver](#document-reference/package-apis/drivers/qemu)
      - [Raspberry Pi driver](#document-reference/package-apis/drivers/raspberrypi)
      - [SDWire driver](#document-reference/package-apis/drivers/sdwire)
      - [Shell driver](#document-reference/package-apis/drivers/shell)
      - [SNMP driver](#document-reference/package-apis/drivers/snmp)
      - [Tasmota driver](#document-reference/package-apis/drivers/tasmota)
      - [TFTP driver](#document-reference/package-apis/drivers/tftp)
      - [U-Boot driver](#document-reference/package-apis/drivers/uboot)
      - [Ustreamer driver](#document-reference/package-apis/drivers/ustreamer)
      - [Yepkit driver](#document-reference/package-apis/drivers/yepkit)
    - [Exceptions](#document-reference/package-apis/exceptions)

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Welcome to Jumpstarter[¶](#welcome-to-jumpstarter "Link to this heading")

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/jumpstarter-dev/jumpstarter) [![Python Packages](https://img.shields.io/badge/PyPI-Packages-blue?logo=pypi)](https://pypi.org/project/jumpstarter/) [![Matrix Chat](https://img.shields.io/matrix/jumpstarter%3Amatrix.org?color=blue)](index.html#jumpstarter:matrix.org) [![Etherpad Notes](https://img.shields.io/badge/Etherpad-Notes-blue?logo=etherpad)](https://etherpad.jumpstarter.dev/pad-lister) [![Weekly Meeting](https://img.shields.io/badge/Weekly%20Meeting-Google%20Meet-blue?logo=google-meet)](https://meet.google.com/gzd-hhbd-hpu)

Jumpstarter is a free and open source testing tool that bridges the gap between development workflows and deployment environments. It enables you to test your software stack consistently across both real hardware and virtual environments using cloud native principles. See Jumpstarter in action:

One tool, any target. Jumpstarter decouples devices from test runners, letting you use identical automation scripts everywhere - your *Makefile* for device testing.

- 🧪 **Unified Testing** - One tool for local, virtual, and remote hardware
- 🐍 **Python-Powered** - Leverage Python’s testing ecosystem
- 🔌 **Hardware Abstraction** - Simplify complex hardware interfaces with drivers
- 🌐 **Collaborative** - Share test hardware globally
- ⚙️ **CI/CD Ready** - Works with cloud native developer environments and pipelines
- 💻 **Cross-Platform** - Supports Linux and macOS

Ready to get started? Use the navigation menu to find documentation that fits your needs.

## Introduction[¶](#introduction "Link to this heading")

Jumpstarter is an open source framework that brings enterprise-grade testing capabilities to everyone. While established industries like automotive and manufacturing have long used HiL testing, these tools have typically been expensive proprietary systems. Jumpstarter democratizes this technology through a free, cloud native approach that works with both physical hardware and virtual devices.

At its core, Jumpstarter uses a client/server architecture where a single client can control multiple devices under test. Its modular design supports both local development (devices connected directly to your machine) and distributed testing environments (devices accessed remotely through a central controller). All communication happens over gRPC, providing a consistent interface regardless of deployment model.

Built on Python, Jumpstarter integrates easily with existing development workflows and runs almost anywhere. It works with common testing tools like [pytest](https://docs.pytest.org/en/stable/), shell scripts, Makefiles, and typical CI/CD systems. Beyond testing, it can function as a virtual KVM (Keyboard, Video, Mouse) switch, enabling remote access to physical devices for development.

### Core Components[¶](#core-components "Link to this heading")

Jumpstarter architecture is based on the following key components:

- Device Under Test (DUT) - Hardware or virtual device being tested
- [Drivers](#document-introduction/drivers) - Interfaces for DUT communication
- [Adapters](#document-introduction/adapters) - Convert driver connections into various formats
- [Exporters](#document-introduction/exporters) - Expose device interfaces over network via gRPC
- [Clients](#document-introduction/clients) - Libraries and CLI tools for device interaction
- [Service](#document-introduction/service) - Kubernetes controller for resource management

Component interactions include:

- **DUT and Drivers** - Drivers provide standardized interfaces to DUT’s hardware connections
- **Drivers and Adapters** - Adapters transform driver connections for specialized use cases
- **Drivers/Adapters and Exporters** - Exporters manage drivers/adapters and expose them via gRPC
- **Exporters and Clients** - Clients connect to exporters to control devices
- **Clients/Exporters and Service** - Service manages access control and resource allocation in distributed mode

Together, these components form a comprehensive testing framework that bridges the gap between development and deployment environments.

### Operation Modes[¶](#operation-modes "Link to this heading")

Building on these components, Jumpstarter implements two operation modes that provide flexibility for different scenarios: *local* and *distributed* modes.

#### Local Mode[¶](#local-mode "Link to this heading")

In local mode, clients communicate directly with exporters running on the same machine or through direct network connections.

```
        ---
config:
  theme: base
  themeVariables:
    lineColor: '#3d94ff'
    primaryBorderColor: '#e5e5e5'
    primaryColor: '#f8f8f8'
    primaryTextColor: '#000'
    secondaryColor: '#f8f8f8'
    tertiaryColor: '#fff'

---
flowchart TB
    subgraph "Developer Machine"
        Client["Client\n(Python Library/CLI)"]
        Exporter["Exporter\n(Local Service)"]
    end

    subgraph "Target Devices"
        DUT["Physical/Virtual\nDevice Under Test"]
        Power["Power Interface"]
        Serial["Serial Interface"]
        Storage["Storage Interface"]
    end

    Client <--> |"gRPC via Socket"| Exporter
    Exporter --> Power
    Exporter --> Serial
    Exporter --> Storage
    Power --> DUT
    Serial --> DUT
    Storage --> DUT
    
```

This mode is ideal for individual developers working directly with accessible hardware or virtual devices. When no client configuration or environment variables are present, Jumpstarter runs in local mode and communicates with a built-in exporter service via a local socket connection, requiring no Kubernetes or other infrastructure. Developers can work with devices on their desk, develop drivers, create automation scripts, and test with QEMU or other virtualization tools.

```
$ jmp shell --exporter my-exporter
$ pytest test_device.py
```

The example above shows typical local mode usage: first connecting to an exporter (which manages the device interfaces) using the `jmp shell` command, and then running tests against the device with pytest. The `--exporter` flag specifies which exporter configuration to use, allowing you to easily switch between different hardware or virtual device setups.

#### Distributed Mode[¶](#distributed-mode "Link to this heading")

Distributed mode enables multiple teams to securely share hardware resources across a network. It uses a Kubernetes-based controller to coordinate access to exporters, managing leases that grant exclusive access to DUT resources, while JWT token-based authentication secures all connections between clients and exporters.

```
        ---
config:
  theme: base
  themeVariables:
    lineColor: '#3d94ff'
    primaryBorderColor: '#e5e5e5'
    primaryColor: '#f8f8f8'
    primaryTextColor: '#000'
    secondaryColor: '#f8f8f8'
    tertiaryColor: '#fff'

---
flowchart TB
    subgraph "Kubernetes Cluster"
        Controller["Controller\nResource Management"]
        Router["Router\nMessage Routing"]
        Auth["Authentication\nJWT Tokens"]
    end

    subgraph "Test Runners"
        Client1["Client 1\n(CI Pipeline)"]
        Client2["Client 2\n(Developer)"]
    end

    subgraph "Lab Resources"
        Exporter1["Exporter 1\n(Physical Hardware)"]
        Exporter2["Exporter 2\n(Virtual Devices)"]
        subgraph "Devices"
            DUT1["Physical Device 1"]
            DUT2["Physical Device 2"]
            DUT3["Virtual Device"]
        end
    end

    Client1 <--> |"JWT Authentication"| Auth
    Client2 <--> |"JWT Authentication"| Auth
    Exporter1 <--> |"JWT Authentication"| Auth
    Exporter2 <--> |"JWT Authentication"| Auth
    Auth <--> Controller

    Client1 <--> |"gRPC (Authorized)"| Controller
    Client2 <--> |"gRPC (Authorized)"| Controller
    Controller <--> Router
    Router <--> |"gRPC"| Exporter1
    Router <--> |"gRPC"| Exporter2
    Exporter1 --> DUT1
    Exporter1 --> DUT2
    Exporter2 --> DUT3
    
```

Distributed mode is ideal for environments where teams need to share hardware resources, especially in CI/CD pipelines requiring scheduled device testing. It excels in geographically distributed test environments where devices are spread across multiple locations, and in any scenario requiring centralized management of testing resources. All these scenarios require a robust security model to manage access rights and prevent resource conflicts.

To address these security needs, the distributed mode implements a comprehensive authentication system that secures access through:

- **Client Registration** - Clients register in the Kubernetes cluster with unique identities
- **Token Issuance** - Controller issues JWT tokens to authenticated clients and exporters
- **Secure Communication** - All gRPC communication between components uses token authentication
- **Access Control** - Controller enforces permissions based on token identity:
  
  - Which exporters a client can lease
  - What actions a client can perform
  - Which driver packages can be loaded

This security model enables dynamic registration of clients and exporters, allowing fine-grained access control in multi-user environments. For example, CI pipelines can be granted access only to specific exporters based on their credentials, ensuring proper resource isolation in shared testing environments.

The following example shows how to run tests in distributed mode:

```
$ jmp config client use my-client
$ jmp create lease --selector vendor=acme,model=widget-v2
$ pytest test_device.py
```

The example above demonstrates the distributed mode workflow: first configuring the client with connection information for the central controller, then requesting a lease on an exporter that matches specific criteria (using selector labels), and finally running tests against the acquired DUT. The lease system ensures exclusive access to the requested resources for the duration of testing, preventing conflicts with other users or pipelines in the shared environment.

##### Drivers[¶](#drivers "Link to this heading")

Jumpstarter uses a modular driver model to build abstractions around the interfaces used to interact with target devices, both physical hardware and virtual systems.

An [Exporter](#document-introduction/exporters) uses Drivers to “export” these interfaces from a host machine to the clients via [gRPC](https://grpc.io/). Drivers can be thought of as a simplified API for an interface or device type.

###### Architecture[¶](#architecture "Link to this heading")

Drivers in Jumpstarter follow a client/server architecture where:

- Driver implementations run on the exporter side and interact directly with hardware or virtual devices
- Driver clients run on the client side and communicate with drivers via gRPC
- Interface classes define the contract between implementations and clients

The architecture follows a pattern with these key components:

- **Interface Class** - An abstract base class using Python’s ABCMeta to define the contract (methods and their signatures) that driver implementations must fulfill. The interface also specifies the client class through the `client()` class method.
- **Driver Class** - Inherits from both the Interface and the base `Driver` class, implementing the logic to configure and use hardware interfaces. Driver methods are marked with the `@export` decorator to expose them over the network.
- **Driver Client** - Provides a user-friendly interface that can be used by clients to interact with the driver either locally or remotely over the network.

When a client requests a lease and connects to an exporter, a session is created for all tests the client needs to execute. Within this session, the specified `Driver` subclass is instantiated for each configured interface. These driver instances live throughout the session’s duration, maintaining state and executing setup/teardown logic.

On the client side, a `DriverClient` subclass is instantiated for each exported interface. Since clients may run on different machines than exporters, `DriverClient` classes are loaded dynamically when specified in the allowed packages list.

To maintain compatibility, avoid making breaking changes to interfaces. Add new methods when needed but preserve existing signatures. If breaking changes are required, create new interface, client, and driver versions within the same module.

Drivers are often used with [Adapters](#document-introduction/adapters), which transform driver connections into different forms or interfaces for specific use cases.

###### Types[¶](#types "Link to this heading")

The API reference of the documentation provides a complete list of all standard drivers, you can find it here: [Driver API Reference](#document-reference/package-apis/drivers/index).

Some categories of drivers include:

- [System Control](index.html#system-control-drivers): Control power to devices, or general control.
- [Communication](index.html#communication-drivers): Provide protocols for network communication, such as TCP/IP, Serial, CAN bus, etc.
- [Data and Storage](index.html#storage-and-data-drivers): Control storage devices, such as SD cards or USB drives, and data.
- [Media](index.html#media-drivers): Provide interfaces for media capture and playback, such as video or audio.
- [Debug and Programming](index.html#debug-and-programming-drivers): Provide interfaces for debugging and programming devices, such as JTAG or SWD, remote flashing, emulation, etc.
- [Utility](index.html#utility-drivers): Provide utility functions, such as shell driver commands on a exporter.

###### Composite Drivers[¶](#composite-drivers "Link to this heading")

Composite drivers combine multiple lower-level drivers to create higher-level abstractions or specialized workflows. For example, a composite driver might coordinate power cycling, storage re-flashing, and serial communication to automate a device initialization process.

In Jumpstarter, drivers are organized in a tree structure which allows for the representation of complex device configurations that may be found in your environment.

Here’s an example of a composite driver tree:

```
MyHarness         # Custom composite driver for the entire target device harness
├─ TcpNetwork     # TCP Network driver to tunnel port 8000
├─ MyPower        # Custom power driver to control device power
├─ SDWire         # SD Wire storage emulator to enable re-flash on demand
├─ DigitalOutput  # GPIO pin control to send signals to the device
└─ MyDebugger     # Custom debugger interface composite driver
   └─ PySerial    # Serial debugger with PySerial
```

###### Configuration[¶](#configuration "Link to this heading")

Drivers are configured using a YAML Exporter config file, which specifies the drivers to load and the parameters for each. Drivers are distributed as Python packages making it easy to develop and install your own drivers.

Here is an example exporter config that loads drivers for both physical and virtual devices:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: ExporterConfig
metadata:
  namespace: default
  name: demo
endpoint: grpc.jumpstarter.example.com:443
token: xxxxx
export:
  # Physical hardware drivers
  power:
    type: jumpstarter_driver_yepkit.driver.Ykush
    config:
      serial: "YK25838"
      port: "1"

  serial:
    type: "jumpstarter_driver_pyserial.driver.PySerial"
    config:
      url: "/dev/ttyUSB0"
      baudrate: 115200

  # Virtual device drivers
  qemu:
    type: "jumpstarter_driver_qemu.driver.QEMU"
    config:
      image_path: "/var/lib/jumpstarter/images/vm.qcow2"
      memory: "1G"
      cpu_cores: 2
```

###### Communication[¶](#communication "Link to this heading")

Drivers use two primary methods to communicate between client and exporter:

###### Messages[¶](#messages "Link to this heading")

Commands are sent as messages from driver clients to driver implementations, allowing the client to trigger actions or retrieve information from the device. Methods marked with the `@export` decorator are made available over the network.

###### Streams[¶](#streams "Link to this heading")

Drivers can establish streams for continuous data exchange, such as for serial communication or video streaming. This enables real-time interaction with both physical and virtual interfaces across the network. Methods marked with the `@exportstream` decorator create streams for bidirectional communication.

###### Authentication and Security[¶](#authentication-and-security "Link to this heading")

Driver access is controlled through Jumpstarter’s authentication mechanisms:

###### Local Mode Authentication[¶](#local-mode-authentication "Link to this heading")

In local mode, drivers are accessible to any process that can connect to the local Unix socket. This is typically restricted by file system permissions. When running tests locally, authentication is simplified since everything runs in the same user context.

###### Distributed Mode Authentication[¶](#distributed-mode-authentication "Link to this heading")

In distributed mode, authentication is handled through JWT tokens:

- **Client Authentication**: Clients authenticate to the controller using JWT tokens, which establishes their identity and permissions
- **Exporter Authentication**: Similarly, exporters authenticate to the controller with their own tokens
- **Driver Access Control**: The controller enforces access control by only allowing authorized clients to acquire leases on exporters and their drivers
- **Driver Allowlist**: Client configurations can specify which driver packages are allowed to be loaded, preventing unintended execution of untrusted code

###### Driver Package Security[¶](#driver-package-security "Link to this heading")

When using distributed mode, driver security considerations include:

- **Package Verification**: Clients can verify that only trusted driver packages are loaded by configuring allowlists
- **Capability Restrictions**: Access to specific driver functionality can be restricted based on client permissions
- **Session Isolation**: Each client session operates with its own driver instances to prevent interference between users

###### Custom Drivers[¶](#custom-drivers "Link to this heading")

While Jumpstarter comes with drivers for many basic interfaces, custom drivers can be developed for specialized hardware interfaces, emulated environments, or to provide domain-specific abstractions for your use case. Custom drivers follow the same architecture pattern as built-in drivers and can be integrated into the system through the exporter configuration.

###### Example Implementation[¶](#example-implementation "Link to this heading")

```
from sys import modules
from types import SimpleNamespace
from anyio import connect_tcp, sleep
from contextlib import asynccontextmanager
from collections.abc import Generator, AsyncGenerator
from abc import ABCMeta, abstractmethod
from jumpstarter.driver import Driver, export, exportstream
from jumpstarter.client import DriverClient
from jumpstarter.common.utils import serve

# Define an interface with ABCMeta
class GenericInterface(metaclass=ABCMeta):
    @classmethod
    def client(cls) -> str:
        return "example.GenericClient"

    @abstractmethod
    def query(self, param: str) -> str: ...

    @abstractmethod
    def get_data(self) -> Generator[dict, None, None]: ...

    @abstractmethod
    def create_stream(self): ...

# Implement the interface with the Driver base class
class GenericDriver(GenericInterface, Driver):
    @export
    def query(self, param: str) -> str:
        # This could be any device-specific command
        return f"Response for {param}"

    # driver calls can be either sync or async
    @export
    async def async_query(self, param: str) -> str:
        # Example of an async operation with delay
        await sleep(1)
        return f"Async response for {param}"

    @export
    def get_data(self) -> Generator[dict, None, None]:
        # Example of a streaming response - could be sensor data, logs, etc.
        for i in range(3):
            yield {"type": "data", "value": i, "timestamp": f"2023-04-0{i+1}"}

    # stream constructor has to be an AsyncContextManager
    # that yield an anyio.abc.ObjectStream
    @exportstream
    @asynccontextmanager
    async def create_stream(self):
        # This could be any stream connection to a device
        async with await connect_tcp(remote_host="example.com", remote_port=80) as stream:
            yield stream

class GenericClient(DriverClient):
    # client methods are sync
    def query(self, param: str) -> str:
        return self.call("query", param)

    def async_query(self, param: str) -> str:
        # async driver methods can be invoked the same way
        return self.call("async_query", param)

    def get_data(self) -> Generator[dict, None, None]:
        yield from self.streamingcall("get_data")

    # Streams can be used for bidirectional communication
    def with_stream(self, callback):
        with self.stream("create_stream") as stream:
            callback(stream)

modules["example"] = SimpleNamespace(GenericClient=GenericClient)

with serve(GenericDriver()) as client:
    assert client.query("test") == "Response for test"
    assert client.async_query("async test") == "Async response for async test"
    data = list(client.get_data())
    assert len(data) == 3
```

##### Adapters[¶](#adapters "Link to this heading")

Jumpstarter uses adapters to transform network connections established by drivers into different forms or interfaces that are more appropriate for specific use cases.

###### Architecture[¶](#architecture "Link to this heading")

Adapters in Jumpstarter follow a transformation pattern where:

- Adapters take a driver client as input
- They transform the connection into a different interface format
- The transformed interface is exposed to the user in a way that’s tailored for specific scenarios

The architecture consists of these key components:

- **Adapter Base** - Adapters typically follow a context manager pattern using Python’s `with` statement for resource management. Each adapter takes a driver client as input and transforms its connection.
- **Connection Transformation** - Adapters create a new interface on top of an existing driver connection, such as forwarding ports, providing web interfaces, or offering terminal-like access.
- **Resource Lifecycle** - Adapters handle proper setup and teardown of resources, ensuring connections are properly established and cleaned up.

Unlike [Drivers](#document-introduction/drivers), which establish the foundational connections to hardware or virtual interfaces, adapters focus on providing alternative ways to interact with those connections without modifying the underlying drivers. Adapters operate entirely on the client side and transform existing connections rather than establishing new ones directly with hardware or virtual devices.

###### Types[¶](#types "Link to this heading")

Different types of adapters serve different needs:

- **Port Forwarding Adapters** - Convert network connections to local ports or sockets
- **Interactive Adapters** - Provide interactive shells or console-like interfaces
- **Protocol Adapters** - Transform connections to use different protocols (e.g., SSH, VNC)
- **UI Adapters** - Create user interfaces for interacting with devices (e.g., web-based VNC)

Adapters can be composed and extended for more complex scenarios:

- **Chaining adapters**: Use the output of one adapter as the input to another
- **Custom adapters**: Create specialized adapters for specific hardware or software interfaces
- **Extended functionality**: Add logging, monitoring, or security features on top of base adapters

###### Implementation Patterns[¶](#implementation-patterns "Link to this heading")

Adapters typically implement the context manager protocol (`__enter__` and `__exit__`) to ensure proper resource management. The general pattern is:

1. Initialize with a driver client reference
2. Set up the transformed connection in `__enter__`
3. Return the appropriate interface (URL, address, interactive object)
4. Clean up resources in `__exit__`

This allows adapters to be used in `with` statements for clean, deterministic resource handling.

When working with adapters, follow these recommended practices:

1. **Always use context managers** (`with` statements) to ensure proper resource cleanup and prevent resource leaks
2. **Consider security implications** when forwarding ports or providing network access, especially when exposing services to external networks
3. **Implement proper error handling and retries** for robust connections in unstable network environments
4. **Use appropriate timeouts** to prevent hanging connections and ensure responsiveness
5. **Consider performance implications** for long-running connections or high-throughput scenarios, especially in resource-constrained environments

###### Example Implementation[¶](#example-implementation "Link to this heading")

```
from contextlib import contextmanager
import socket
import threading
from typing import Tuple, Any

class TcpPortforwardAdapter:
    """
    Adapter that forwards a remote TCP port to a local TCP port.

    Args:
        client: A network driver client that provides a connection
        local_host: Host to bind to (default: 127.0.0.1)
        local_port: Port to bind to (default: 0, which selects a random port)

    Returns:
        A tuple of (host, port) when used as a context manager
    """
    def __init__(self, client, local_host="127.0.0.1", local_port=0):
        self.client = client
        self.local_host = local_host
        self.local_port = local_port
        self._server = None
        self._thread = None

    def __enter__(self) -> Tuple[str, int]:
        # Create a socket server
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((self.local_host, self.local_port))
        self._server.listen(5)

        # Get the actual port (if we used port 0)
        self.local_host, self.local_port = self._server.getsockname()

        # Start a thread to handle connections
        self._thread = threading.Thread(target=self._handle_connections, daemon=True)
        self._thread.start()

        return (self.local_host, self.local_port)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._server:
            self._server.close()
            self._server = None

        # Thread will exit because it's a daemon
        self._thread = None

    def _handle_connections(self):
        while True:
            try:
                client_socket, _ = self._server.accept()
                # For each connection, establish a connection to the remote
                # and set up bidirectional forwarding
                remote_conn = self.client.connect()
                self._start_forwarding(client_socket, remote_conn)
            except Exception:
                # Server was closed or other error
                break

    def _start_forwarding(self, local_socket, remote_conn):
        # Set up bidirectional forwarding between local_socket and remote_conn
        # Typically done with two threads, one for each direction
        # Implementation details depend on the specific driver client interface
        pass


# Example usage:
def example_usage():
    # Assuming 'client' is a network driver client
    with TcpPortforwardAdapter(client, local_port=8080) as (host, port):
        print(f"Service available at {host}:{port}")
        # The service is now accessible at the local address
        # while this context is active
```

##### Exporters[¶](#exporters "Link to this heading")

Jumpstarter uses a program called an Exporter to enable remote access to your hardware. The Exporter typically runs on a “host” system directly connected to your hardware. It is called an Exporter because it “exports” the interfaces connected to the target device for client access.

###### Hosts[¶](#hosts "Link to this heading")

Typically, the host will be a low-cost test system such as a single board computer with sufficient interfaces to connect to your hardware. It is also possible to use a local high-power server (or CI runner) as the host device.

A host can run multiple Exporter instances simultaneously if it needs to interact with several different devices at the same time.

###### Exporter Configuration[¶](#exporter-configuration "Link to this heading")

Exporters use a YAML configuration file to define which Drivers must be loaded and the configuration required.

Here is an example Exporter config file which would typically be saved at `/etc/jumpstarter/exporters/demo.yaml`:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: ExporterConfig
metadata:
  namespace: default
  name: demo
endpoint: grpc.jumpstarter.example.com:443
token: xxxxx
grpcConfig:
    grpc.keepalive_time_ms: 20000
export:
  power:
    type: jumpstarter_driver_yepkit.driver.Ykush
    config:
      serial: "YK25838"
      port: "1"
  serial:
    type: "jumpstarter_driver_pyserial.driver.PySerial"
    config:
      url: "/dev/ttyUSB0"
      baudrate: 115200
  storage:
    type: "jumpstarter_driver_sdwire.driver.SDWire"
    config:
      serial: "sdw-00001"
      storage_device: "/dev/disk/by-path/..."
  custom:
    type: "vendorpackage.CustomDriver"
    config:
      hello: "world"
  reference:
    ref: "power"
```

Note that the `grpcConfig` section supports all options documented in the [gRPC argument keys documentation](https://grpc.github.io/grpc/core/group__grpc__arg__keys.html).

###### Running an Exporter[¶](#running-an-exporter "Link to this heading")

To run an Exporter on a host system, you must have Python &gt;=3.11 installed and the driver packages specified in the config installed in your current Python environment.

You can run the exporter in your local terminal with:

```
$ jmp run --exporter myexporter
```

Exporters can also be run in a privileged container or as a systemd daemon. It is recommended to run the Exporter service in the background with auto-restart capabilities in case something goes wrong and it needs to be restarted.

##### Clients[¶](#clients "Link to this heading")

To interact with your target device from a development machine or through a CI/CD pipeline, you must use a Jumpstarter client. The Python client can be used either as a library or as a [CLI tool](#document-reference/man-pages/index).

###### Types of Clients[¶](#types-of-clients "Link to this heading")

Jumpstarter supports two types of client configurations: *local* and *remote*.

###### Local Clients[¶](#local-clients "Link to this heading")

When using Jumpstarter in *local-only* mode, you can use the local client functionality to directly access your hardware. The local client will automatically use any drivers that are registered without the need for an exporter instance running in the background.

###### Remote Clients[¶](#remote-clients "Link to this heading")

When using Jumpstarter in *distributed* mode, the client must be configured to connect to an instance of the Service that can authenticate and route requests to the appropriate exporter instance.

The following parameters are required to set up a remote client:

- The URL of a Service endpoint to connect to
- An authentication token generated by the Service

Note

The endpoint must be accessible from your client machine to communicate with the Service.

##### Service[¶](#service "Link to this heading")

When building a lab with many devices under test, it quickly becomes difficult to keep track of devices, schedule access for automated tests, and perform routine maintenance such as batch updates.

Jumpstarter provides a service that can be installed in any [Kubernetes](https://kubernetes.io/) cluster to manage connected clients and exporters.

If you’re already using a Kubernetes-native CI tool such as [Tekton](https://tekton.dev/), [Jenkins X](https://jenkins-x.io/), [Konflux](https://konflux-ci.dev), or [GitLab CI](https://docs.gitlab.com/user/clusters/agent/ci_cd_workflow/), Jumpstarter can integrate directly into your existing cloud or on-premises cluster.

###### Controller[¶](#controller "Link to this heading")

The core of the Service is the Controller, which manages access to devices, authenticates clients/exporters, and maintains a set of labels to easily identify specific devices.

The Controller is implemented as a Kubernetes [controller](https://github.com/jumpstarter-dev/jumpstarter-controller) using [Custom Resource Definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) to store information about clients, exporters, leases, and other resources.

###### Leases[¶](#leases "Link to this heading")

When a client requests access to an exporter and a matching instance is found, a Lease is created. The lease ensures that each lessee (client) has exclusive access to a specific device/exporter.

Clients can be scheduled to access a specific exporter or any exporter that matches a set of requested labels, similar to [node selection](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) in Kubernetes. This enables flexible CI-driven testing even when physical resources are limited.

###### Router[¶](#router "Link to this heading")

The Router service is used by the controller to route messages between clients and exporters through a gRPC tunnel. This enables remote access to exported interfaces via the client.

Once a lease is established, all traffic between the client and the exporter flows through a router instance. While there may only be one controller, the router can be scaled with multiple instances to handle traffic between many clients and exporters simultaneously.

## Getting Started[¶](#getting-started "Link to this heading")

This section provides hands-on guides to start using Jumpstarter in your own environment. The guides cover:

- [Installation](#document-getting-started/installation/index): Setting up Jumpstarter packages and services
- [Configuration](#document-getting-started/configuration/index): Configuring clients, exporters, and authentication
- [Usage](#document-getting-started/usage/index): Running your first tests and integrating with your development workflow

These guides support both local-mode for individual development and distributed-mode for team environments with shared hardware resources.

### Installation[¶](#installation "Link to this heading")

This section provides guidance on installing Jumpstarter components in your environment. The guides cover:

- [Packages](#document-getting-started/installation/packages): Installing Jumpstarter software packages
- [Service](#document-getting-started/installation/service): Setting up Jumpstarter as a Kubernetes service

#### Packages[¶](#packages "Link to this heading")

##### Python[¶](#python "Link to this heading")

Jumpstarter includes the following installable Python packages:

- `jumpstarter`: Core package for exporter interaction and service hosting
- `jumpstarter-cli`: CLI components metapackage including admin and user interfaces
- `jumpstarter-cli-admin`: Admin CLI for controller management and lease control
- `jumpstarter-driver-*`: Drivers for device connectivity
- `jumpstarter-imagehash`: Image checking library for video inputs
- `jumpstarter-testing`: Tools for Jumpstarter-powered pytest integration

###### Installing Release Packages[¶](#installing-release-packages "Link to this heading")

The [Jumpstarter Python packages](https://pkg.jumpstarter.dev/) provide all the tools you need to run an exporter or interact with your hardware as a client.

Install the Python package using `pip` or a similar tool. You need Python &gt;=3.11:

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-all
$ mkdir -p "${HOME}/.config/jumpstarter/"
$ sudo mkdir /etc/jumpstarter
```

The command above installs packages globally. For library usage, we recommend installing in a virtual environment instead:

```
$ python3 -m venv ~/.venv/jumpstarter
$ source ~/.venv/jumpstarter/bin/activate
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-all
```

Additional package indexes are available, this is a complete list of our indexes:

Index

Description

[releases](https://pkg.jumpstarter.dev/)

Release, or release-candidate versions

[main](https://pkg.jumpstarter.dev/main/)

Index tracking the main branch, equivalent to installing from sources

[release-0.6](https://pkg.jumpstarter.dev/release-0.6)

Index tracking a stable branch

###### Installing from Source[¶](#installing-from-source "Link to this heading")

Jumpstarter undergoes active development with frequent feature additions. We conduct thorough testing and recommend installing the latest version from the `main` branch.

```
$ sudo dnf install -y uv make git
$ git clone https://github.com/jumpstarter-dev/jumpstarter.git
$ cd jumpstarter
$ rm .python-version
$ make sync
$ mkdir -p "${HOME}/.config/jumpstarter/"
$ sudo mkdir /etc/jumpstarter
```

Activate the virtual environment to use Jumpstarter CLI commands:

```
$ source .venv/bin/activate
$ jmp version
```

###### Running in a Container[¶](#running-in-a-container "Link to this heading")

If you prefer not to install packages locally, you can use the container package instead. To interact with the service without local Python package installation, create an alias to run the `jmp` client in a container. We recommend adding this alias to your shell profile for persistent use:

```
$ alias jmp='podman run --rm -it -w /home \
    -v "$(pwd):/home":z \
    -v "${HOME}/.config/jumpstarter/:/root/.config/jumpstarter":z \
    quay.io/jumpstarter-dev/jumpstarter:latest jmp'
```

When you need hardware access for running the `jmp` command or following the [local-only workflow](index.html#local-mode), configure the container with device access, host networking, and privileged mode. This typically requires `root` privileges:

```
$ mkdir -p "${HOME}/.config/jumpstarter/" /etc/jumpstarter
$ alias jmp='podman run --rm -it \
    -v "${HOME}/.config/jumpstarter/:/root/.config/jumpstarter":z \
    --net=host --privileged \
    -v /run/udev:/run/udev -v /dev:/dev -v /etc/jumpstarter:/etc/jumpstarter:z \
    quay.io/jumpstarter-dev/jumpstarter:latest jmp'
```

If you’ve configured a `jmp` alias you can undefine it with:

```
$ unalias jmp
```

#### Service[¶](#service "Link to this heading")

This section explains how to install and configure the Jumpstarter service in your Kubernetes cluster. The service enables centralized management of your Jumpstarter environment. Before installing, ensure you have:

- A Kubernetes cluster available
- `kubectl` installed and configured to access your cluster
- [Helm](https://helm.sh/docs/intro/install/) (version 3.x or newer)
- Administrator access to your cluster (required for CRD installation)
- Domain name for service endpoints (or use `nip.io` for local testing)

Note

`global.baseDomain` creates these service hostnames with `jumpstarter.example.com`:

- `grpc.jumpstarter.example.com`
- `router.jumpstarter.example.com` (for router endpoints)

##### Kubernetes with Helm[¶](#kubernetes-with-helm "Link to this heading")

Install Jumpstarter on a standard Kubernetes cluster using Helm:

```
$ helm upgrade jumpstarter --install oci://quay.io/jumpstarter-dev/helm/jumpstarter \
        --create-namespace --namespace jumpstarter-lab \
        --set global.baseDomain=jumpstarter.example.com \
        --set global.metrics.enabled=true \
        --set jumpstarter-controller.grpc.mode=ingress \
        --version=0.6.0
```

##### OpenShift with Helm[¶](#openshift-with-helm "Link to this heading")

Install Jumpstarter on an OpenShift cluster using Helm:

```
$ helm upgrade jumpstarter --install oci://quay.io/jumpstarter-dev/helm/jumpstarter \
          --create-namespace --namespace jumpstarter-lab \
          --set global.baseDomain=jumpstarter.example.com \
          --set global.metrics.enabled=true \
          --set jumpstarter-controller.grpc.mode=route \
          --version=0.6.0
```

##### OpenShift with ArgoCD[¶](#openshift-with-argocd "Link to this heading")

First, create and label a namespace for Jumpstarter:

```
$ kubectl create namespace jumpstarter-lab
$ kubectl label namespace jumpstarter-lab argocd.argoproj.io/managed-by=openshift-gitops
```

For ArgoCD to manage Jumpstarter CRDs, create this ClusterRole and ClusterRoleBinding:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    argocds.argoproj.io/name: openshift-gitops
    argocds.argoproj.io/namespace: openshift-gitops
  name: openshift-gitops-argocd-appcontroller-crd
rules:
- apiGroups:
  - 'apiextensions.k8s.io'
  resources:
  - 'customresourcedefinitions'
  verbs:
  - '*'
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  annotations:
    argocds.argoproj.io/name: openshift-gitops
    argocds.argoproj.io/namespace: openshift-gitops
  name: openshift-gitops-argocd-appcontroller-crd
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: openshift-gitops-argocd-appcontroller-crd
subjects:
- kind: ServiceAccount
  name: openshift-gitops-argocd-application-controller
  namespace: openshift-gitops
```

Create an ArgoCD Application to deploy Jumpstarter:

Warning

The secrets `jumpstarter-controller.controllerSecret` and `jumpstarter-controller.routerSecret` must be unique for each installation. While Helm can auto-generate these, ArgoCD cannot - you must manually create these in your Jumpstarter namespace.

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: jumpstarter
  namespace: openshift-gitops
spec:
  destination:
    name: in-cluster
    namespace: jumpstarter-lab
  project: default
  source:
    chart: jumpstarter
    helm:
      parameters:
      - name: global.baseDomain
        value: devel.jumpstarter.dev
      - name: global.metrics.enabled
        value: "true"
      - name: jumpstarter-controller.controllerSecret
        value: "pick-a-secret-DONT-USE-THIS-DEFAULT"
      - name: jumpstarter-controller.routerSecret
        value: "again-pick-a-secret-DONT-USE-THIS-DEFAULT"
      - name: jumpstarter-controller.grpc.mode
        value: "route"
    repoURL: quay.io/jumpstarter-dev/helm
    targetRevision: "0.6.0"
```

##### Local cluster with Minikube[¶](#local-cluster-with-minikube "Link to this heading")

Minikube runs local Kubernetes clusters using VMs or container “nodes”. It works across several platforms and supports different hypervisors, making it ideal for local development and testing.

Find more information on the [minikube website](https://minikube.sigs.k8s.io/docs/start/).

###### Create a minikube cluster[¶](#create-a-minikube-cluster "Link to this heading")

Expand the default NodePort range to include the Jumpstarter ports:

```
$ minikube start --extra-config=apiserver.service-node-port-range=8000-9000
```

###### Install Jumpstarter with the CLI[¶](#install-jumpstarter-with-the-cli "Link to this heading")

The Jumpstarter CLI’s `jmp admin install` command simplifies installation in your Kubernetes cluster.

Use the minikube IP address when installing with the CLI:

```
$ jmp admin install --ip $(minikube ip)
```

For complete documentation of the `jmp admin install` command and all available options, see the [MAN pages](#document-reference/man-pages/jmp).

###### Install Jumpstarter with Helm[¶](#install-jumpstarter-with-helm "Link to this heading")

For manual installation with Helm, use these commands:

```
$ export IP=$(minikube ip)
$ export BASEDOMAIN="jumpstarter.${IP}.nip.io"
$ export GRPC_ENDPOINT="grpc.${BASEDOMAIN}:8082"
$ export GRPC_ROUTER_ENDPOINT="router.${BASEDOMAIN}:8083"
$ helm upgrade jumpstarter --install oci://quay.io/jumpstarter-dev/helm/jumpstarter \
    --create-namespace --namespace jumpstarter-lab \
    --set global.baseDomain=${BASEDOMAIN} \
    --set jumpstarter-controller.grpc.endpoint=${GRPC_ENDPOINT} \
    --set jumpstarter-controller.grpc.routerEndpoint=${GRPC_ROUTER_ENDPOINT} \
    --set global.metrics.enabled=false \
    --set jumpstarter-controller.grpc.nodeport.enabled=true \
    --set jumpstarter-controller.grpc.nodeport.port=8082 \
    --set jumpstarter-controller.grpc.nodeport.routerPort=8083 \
    --set jumpstarter-controller.grpc.mode=nodeport \
    --version=0.6.0
```

##### Local cluster with kind[¶](#local-cluster-with-kind "Link to this heading")

To try the Jumpstarter Controller on your local machine, run a local Kubernetes cluster for development purposes.

kind is a tool for running local Kubernetes clusters using Podman or Docker container “nodes”.

Tip

Consider minikube for environments requiring [untrusted certificates](https://minikube.sigs.k8s.io/docs/handbook/untrusted_certs/).

Find more information on the [kind website](https://kind.sigs.k8s.io/docs/user/quick-start/).

###### Create a kind cluster[¶](#create-a-kind-cluster "Link to this heading")

First, create a kind cluster config that enables nodeports to host the Services. Save this as `kind_config.yaml`:

```
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
kubeadmConfigPatches:
- |
  kind: ClusterConfiguration
  apiServer:
    extraArgs:
      "service-node-port-range": "3000-32767"
- |
  kind: InitConfiguration
  nodeRegistration:
    kubeletExtraArgs:
      node-labels: "ingress-ready=true"
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 80
    hostPort: 5080
    protocol: TCP
  - containerPort: 30010
    hostPort: 8082
    protocol: TCP
  - containerPort: 30011
    hostPort: 8083
    protocol: TCP
  - containerPort: 443
    hostPort: 5443
    protocol: TCP
```

Next, create a kind cluster using the config you created:

```
$ kind create cluster --config kind_config.yaml
```

###### Install Jumpstarter with the CLI[¶](#id1 "Link to this heading")

The Jumpstarter CLI provides the `jmp admin install` command to automatically run Helm with the correct arguments, simplifying installation in your Kubernetes cluster.

Install Jumpstarter with default options:

```
$ jmp admin install
```

For complete documentation of the `jmp admin install` command and all available options, see the [MAN pages](#document-reference/man-pages/jmp).

###### Install Jumpstarter with Helm[¶](#id2 "Link to this heading")

If you prefer manual installation with Helm, use the following commands:

```
$ export IP="X.X.X.X"
$ export BASEDOMAIN="jumpstarter.${IP}.nip.io"
$ export GRPC_ENDPOINT="grpc.${BASEDOMAIN}:8082"
$ export GRPC_ROUTER_ENDPOINT="router.${BASEDOMAIN}:8083"
$ helm upgrade jumpstarter --install oci://quay.io/jumpstarter-dev/helm/jumpstarter \
            --create-namespace --namespace jumpstarter-lab \
            --set global.baseDomain=${BASEDOMAIN} \
            --set jumpstarter-controller.grpc.endpoint=${GRPC_ENDPOINT} \
            --set jumpstarter-controller.grpc.routerEndpoint=${GRPC_ROUTER_ENDPOINT} \
            --set global.metrics.enabled=false \
            --set jumpstarter-controller.grpc.nodeport.enabled=true \
            --set jumpstarter-controller.grpc.mode=nodeport \
            --version=0.6.0
```

### Configuration[¶](#configuration "Link to this heading")

This section explains how to configure Jumpstarter for your environment.

- [Files](#document-getting-started/configuration/files): Understanding the structure and content of configuration files
- [Loading Order](#document-getting-started/configuration/loading-order): Understanding how configuration files are prioritized from different sources (environment variables, command line, system and user config files)
- [Authentication](#document-getting-started/configuration/authentication): Setting up OIDC and managing tokens

For a list of supported configuration options including an explanation please refer to the [MAN pages](#document-reference/man-pages/index).

#### Files[¶](#files "Link to this heading")

This page describes configuration files used in Jumpstarter, including their format, location, related environment variables, and management commands.

Jumpstarter follows a specific hierarchy when loading configurations. See [Loading Order](#document-getting-started/configuration/loading-order) for details on how configurations from different sources are prioritized.

##### User Configuration[¶](#user-configuration "Link to this heading")

**File**: `config.yaml`  
**Location**: `~/.config/jumpstarter/config.yaml`  
**Description**: Defines global user settings including current client selection.

**Format**:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: UserConfig
config:
  current-client: default
```

**CLI Commands**: Modified through `jmp config` commands.

##### Client Configuration[¶](#client-configuration "Link to this heading")

**File**: Various files with `.yaml` extension  
**Location**: `~/.config/jumpstarter/clients/*.yaml`  
**Description**: Stores client configurations including endpoints, access tokens, and driver settings.

**Format**:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: Client
metadata:
  name: myclient
  namespace: jumpstarter-lab
tls:
  insecure: false
  ca: ""
endpoint: "jumpstarter.my-lab.com:1443"
token: "dGhpc2lzYXRva2VuLTEyMzQxMjM0MTIzNEyMzQtc2Rxd3Jxd2VycXdlcnF3ZXJxd2VyLTEyMzQxMjM0MTIz"
drivers:
  allow: ["jumpstarter_drivers_*", "vendorpackage.*"]
```

**Environment Variables**:

- `JUMPSTARTER_GRPC_INSECURE` - Set to `1` to disable TLS verification
- `JMP_CLIENT_CONFIG` - Path to a client configuration file
- `JMP_CLIENT` - Name of a registered client config
- `JMP_NAMESPACE` - Namespace in the controller
- `JMP_NAME` - Client name
- `JMP_ENDPOINT` - gRPC endpoint (overrides config file)
- `JMP_TOKEN` - Auth token (overrides config file)
- `JMP_DRIVERS_ALLOW` - Comma-separated list of allowed driver namespaces
- `JUMPSTARTER_FORCE_SYSTEM_CERTS` - Set to `1` to force system CA certificates

**CLI Commands**:

```
$ jmp config client create <name>  # Create new client config
$ jmp config client use <name>     # Switch to a different client
$ jmp config client list           # List available clients
$ jmp config client delete <name>  # Remove a client config
```

##### Exporter Configuration[¶](#exporter-configuration "Link to this heading")

**File**: Various files with `.yaml` extension  
**Location**: `/etc/jumpstarter/exporters/*.yaml`  
**Description**: Defines exporter settings including connection details and driver configurations.

**Format**:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: Exporter
metadata:
  name: myexporter
  namespace: jumpstarter-lab
tls:
  insecure: false
  ca: ""
endpoint: "jumpstarter.my-lab.com:1443"
token: "dGhpc2lzYXRva2VuLTEyMzQxMjM0MTIzNEyMzQtc2Rxd3Jxd2VycXdlcnF3ZXJxd2VyLTEyMzQxMjM0MTIz"
export:
  power:
    type: "jumpstarter_driver_power.driver.PduPower"
    config:
      host: "192.168.1.111"
      port: 1234
      username: "admin"
      password: "secret"
  serial:
    type: "jumpstarter_driver_pyserial.driver.PySerial"
    config:
      url: "/dev/ttyUSB0"
      baudrate: 115200
```

**Environment Variables**:

- `JUMPSTARTER_GRPC_INSECURE` - Set to `1` to disable TLS verification
- `JMP_ENDPOINT` - gRPC endpoint (overrides config file)
- `JMP_TOKEN` - Auth token (overrides config file)
- `JMP_NAMESPACE` - Namespace in the controller
- `JMP_NAME` - Exporter name

**CLI Commands**:

```
$ jmp config exporter create <name>   # Create new exporter config
$ jmp config exporter list            # List available exporters
$ jmp config exporter delete <name>   # Remove an exporter config
```

##### Running Exporters[¶](#running-exporters "Link to this heading")

Exporters can be run manually or as system services:

```
# Run with specific exporter config
$ jmp run --exporter my-exporter

# Or specify a config path directly
$ jmp run --exporter-config /etc/jumpstarter/exporters/my-exporter.yaml
```

For persistent operation, exporters can be installed as systemd services using podman-systemd. Create a systemd service file at `/etc/containers/systemd/my-exporter.container` with the following content:

```
[Unit]
Description=My exporter
[Container]
ContainerName=my-exporter
Exec=/jumpstarter/bin/jmp run --exporter my-exporter
Image=quay.io/jumpstarter-dev/jumpstarter:latest
Network=host
PodmanArgs=--privileged
Volume=/run/udev:/run/udev
Volume=/dev:/dev
Volume=/etc/jumpstarter:/etc/jumpstarter
[Service]
Restart=always
StartLimitBurst=0
[Install]
WantedBy=multi-user.target default.target
```

Then enable and start the service:

```
$ sudo systemctl daemon-reload
$ sudo systemctl enable --now my-exporter
```

#### Loading Order[¶](#loading-order "Link to this heading")

Jumpstarter uses a hierarchical approach to loading configuration, allowing you to override settings at different levels.

##### Configuration Sources[¶](#configuration-sources "Link to this heading")

Jumpstarter loads configuration from the following sources, in order of precedence (highest to lowest):

1. **Command-line arguments** - Highest priority, override all other settings
2. **Environment variables** - Override file-based configurations
3. **User configuration files** - Located in `${HOME}/.config/jumpstarter/`
4. **System configuration files** - Located in `/etc/jumpstarter/`

##### Client Configuration Hierarchy[¶](#client-configuration-hierarchy "Link to this heading")

For client operations, Jumpstarter processes configurations in this order:

1. **Command-line options** such as `--endpoint` or `--client-config`
2. **Environment variables** such as `JMP_ENDPOINT`, `JMP_TOKEN`, or `JMP_CLIENT_CONFIG`
3. **Current client** defined in `${HOME}/.config/jumpstarter/config.yaml`
4. **Specific client file** in `${HOME}/.config/jumpstarter/clients/<n>.yaml`

##### Exporter Configuration Hierarchy[¶](#exporter-configuration-hierarchy "Link to this heading")

For exporter operations, Jumpstarter processes configurations in this order:

1. **Command-line options** such as `--exporter` or `--exporter-config`
2. **Environment variables** such as `JMP_ENDPOINT`, `JMP_TOKEN`, or `JMP_NAMESPACE`
3. **Specific exporter file** in `/etc/jumpstarter/exporters/<n>.yaml`

##### Example[¶](#example "Link to this heading")

Here’s a practical example of how configuration overrides work:

1. You create a client configuration file at `${HOME}/.config/jumpstarter/clients/default.yaml`:
   
   ```
   endpoint: "jumpstarter1.my-lab.com:1443"
   ```
2. You set an environment variable in your terminal:
   
   ```
   $ export JMP_ENDPOINT="jumpstarter2.my-lab.com:1443"
   ```
3. You run a command with an explicit endpoint argument:
   
   ```
   $ jmp --endpoint jumpstarter3.my-lab.com:1443 info
   ```

Jumpstarter connects to `jumpstarter3.my-lab.com:1443` because the command-line argument has the highest priority.

##### Use Cases[¶](#use-cases "Link to this heading")

Choose the appropriate configuration method based on your needs:

- **Development**: Use user config files for personal settings
- **CI/CD Pipelines**: Use environment variables for automation
- **One-off Tasks**: Use command-line arguments for temporary changes
- **System Defaults**: Use system config files for shared settings across users

This hierarchical approach allows Jumpstarter to be flexible across different usage scenarios while maintaining consistent behavior.

#### Authentication[¶](#authentication "Link to this heading")

Jumpstarter uses internally issued JWT tokens to authenticate clients and exporters by default. You can also configure Jumpstarter to use external OpenID Connect (OIDC) providers.

To use OIDC with your Jumpstarter installation:

1. Set the helm value `jumpstarter-controller.authenticationConfiguration` to a valid `AuthenticationConfiguration` yaml configuration
2. Configure your OIDC provider to work with Jumpstarter
3. Create users with appropriate OIDC usernames

##### Examples[¶](#examples "Link to this heading")

###### Keycloak[¶](#keycloak "Link to this heading")

Set up Keycloak for Jumpstarter authentication:

1. Create a new Keycloak client with these settings:
   
   - `Client ID`: `jumpstarter-cli`
   - `Valid redirect URIs`: `http://localhost/callback`
   - Leave remaining fields as default
2. Use this configuration for `jumpstarter-controller.authenticationConfiguration` during installation:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: AuthenticationConfiguration
jwt:
- issuer:
    url: https://<keycloak domain>/realms/<realm name>
    certificateAuthority: <PEM encoded CA certificates>
    audiences:
    - jumpstarter-cli
  claimMappings:
    username:
      claim: preferred_username
      prefix: "keycloak:"
```

Note, the HTTPS URL is mandatory, and you only need to include certificateAuthority when using a self-signed certificate. The username will be prefixed with “keycloak:” (e.g., keycloak:example-user).

3. Create clients and exporters with the `jmp admin create` commands. Be sure to prefix usernames with `keycloak:` as configured in the claim mappings:

```
$ jmp admin create client test-client --insecure-tls-config --oidc-username keycloak:developer-1
```

4. Instruct users to log in with:

```
$ jmp login --client <client alias> \
    --insecure-tls-config \
    --endpoint <jumpstarter controller endpoint> \
    --namespace <namespace> --name <client name> \
    --issuer https://<keycloak domain>/realms/<realm name>
```

For non-interactive login, add username and password:

```
$ jmp login --client <client alias> [other parameters] \
    --insecure-tls-config \
    --username <username> \
    --password <password>
```

For machine-to-machine authentication (useful in CI environments), use a token:

```
$ jmp login --client <client alias> [other parameters] --token <token>
```

For exporters, use similar login command but with the `--exporter` flag:

```
$ jmp login --exporter <exporter alias> \
    --insecure-tls-config \
    --endpoint <jumpstarter controller endpoint> \
    --namespace <namespace> --name <exporter name> \
    --issuer https://<keycloak domain>/realms/<realm name>
```

###### Dex[¶](#dex "Link to this heading")

Follow these steps to set up Dex for service account authentication:

1. Initialize a self-signed CA and sign certificate for Dex:

```
$ easyrsa init-pki
$ easyrsa --no-pass build-ca
$ easyrsa --no-pass build-server-full dex.dex.svc.cluster.local
```

Then import the certificate into a Kubernetes secret:

```
$ kubectl create namespace dex
$ kubectl -n dex create secret tls dex-tls \
    --cert=pki/issued/dex.dex.svc.cluster.local.crt \
    --key=pki/private/dex.dex.svc.cluster.local.key
```

2. Install Dex with Helm using the following `values.yaml`:

```
https:
  enabled: true
config:
  issuer: https://dex.dex.svc.cluster.local:5556
  web:
    tlsCert: /etc/dex/tls/tls.crt
    tlsKey: /etc/dex/tls/tls.key
  storage:
    type: kubernetes
    config:
      inCluster: true
  staticClients:
    - id: jumpstarter-cli
      name: Jumpstarter CLI
      public: true
  connectors:
    - name: kubernetes
      type: oidc
      id: kubernetes
      config:
        # kubectl get --raw /.well-known/openid-configuration | jq -r '.issuer'
        issuer: "https://kubernetes.default.svc.cluster.local"
        rootCAs:
          - /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        userNameKey: sub
        scopes:
          - profile
volumes:
  - name: tls
    secret:
      secretName: dex-tls
volumeMounts:
  - name: tls
    mountPath: /etc/dex/tls
service:
  type: ClusterIP
  ports:
    http:
      port: 5554
    https:
      port: 5556
```

Ensure OIDC discovery URLs do not require authentication:

```
$ kubectl create clusterrolebinding oidc-reviewer  \
    --clusterrole=system:service-account-issuer-discovery \
    --group=system:unauthenticated
```

Then install Dex:

```
$ helm repo add dex https://charts.dexidp.io
$ helm install --namespace dex --wait -f values.yaml dex dex/dex
```

3. Configure Jumpstarter to trust Dex. Use this configuration for `jumpstarter-controller.authenticationConfiguration` during installation:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: AuthenticationConfiguration
jwt:
  - issuer:
      url: https://dex.dex.svc.cluster.local:5556
      audiences:
      - jumpstarter-cli
      audienceMatchPolicy: MatchAny
      certificateAuthority: |
        <content of pki/ca.crt>
    claimMappings:
      username:
        claim: "name"
        prefix: "dex:"
```

4. Create clients and exporters with appropriate OIDC usernames. Prefix the full service account name with “dex:” as configured in the claim mappings.:

```
$ jmp admin create exporter test-exporter --label foo=bar \
    --insecure-tls-config \
    --oidc-username dex:system:serviceaccount:default:test-service-account
```

5. Configure pods with proper service accounts to log in using:

For clients:

```
$ jmp login --client <client alias> \
    --insecure-tls-config \
    --endpoint <jumpstarter controller endpoint> \
    --namespace <namespace> --name <client name> \
    --issuer https://dex.dex.svc.cluster.local:5556 \
    --connector-id kubernetes \
    --token $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
```

For exporters:

```
$ jmp login --exporter <exporter alias> \
    --insecure-tls-config \
    --endpoint <jumpstarter controller endpoint> \
    --namespace <namespace> --name <exporter name> \
    --issuer https://dex.dex.svc.cluster.local:5556 \
    --connector-id kubernetes \
    --token $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
```

##### Reference[¶](#reference "Link to this heading")

The reference section provides a complete example of an `AuthenticationConfiguration` resource with detailed comments. Use this as a template for creating your own configuration.

Key components include:

- JWT issuer configuration
- Claim validation rules
- Claim mappings for username and groups
- User validation rules

```
apiVersion: jumpstarter.dev/v1alpha1
kind: AuthenticationConfiguration
# JWT authenticators for OIDC-issued tokens
jwt:
- issuer:
    # URL of the OIDC provider (must use https://)
    url: https://example.com
    # Optional: override URL for discovery information
    discoveryURL: https://discovery.example.com/.well-known/openid-configuration
    # Optional: PEM encoded CA certificates for validation
    certificateAuthority: <PEM encoded CA certificates>
    # List of acceptable token audiences
    audiences:
    - my-app
    - my-other-app
    # Required when multiple audiences are specified
    audienceMatchPolicy: MatchAny
  # rules applied to validate token claims to authenticate users.
  claimValidationRules:
    # Validate specific claim values
  - claim: hd
    requiredValue: example.com
    # Alternative: use CEL expressions for complex validation
  - expression: 'claims.hd == "example.com"'
    message: the hd claim must be set to example.com
  - expression: 'claims.exp - claims.nbf <= 86400'
    message: total token lifetime must not exceed 24 hours
  # Map OIDC claims to Jumpstarter user properties
  claimMappings:
    # Required: configure username mapping
    username:
      # JWT claim to use as username
      claim: "sub"
      # Prefix for username (required when claim is set)
      prefix: ""
      # Alternative: use CEL expression (mutually exclusive with claim+prefix)
      # expression: 'claims.username + ":external-user"'
    # Optional: configure groups mapping
    groups:
      claim: "sub"
      prefix: ""
      # Alternative: use CEL expression
      # expression: 'claims.roles.split(",")'
    # Optional: configure UID mapping
    uid:
      claim: 'sub'
      # Alternative: use CEL expression
      # expression: 'claims.sub'
    # Optional: add extra attributes to UserInfo
    extra:
    - key: 'example.com/tenant'
      valueExpression: 'claims.tenant'
  # validation rules applied to the final user object.
  userValidationRules:
  - expression: "!user.username.startsWith('system:')"
    message: 'username cannot used reserved system: prefix'
  - expression: "user.groups.all(group, !group.startsWith('system:'))"
    message: 'groups cannot used reserved system: prefix'
```

### Usage[¶](#usage "Link to this heading")

This section provides guidance on how to use Jumpstarter effectively in your development workflow. The guides cover:

- [Setup Local Mode](#document-getting-started/usage/setup-local-mode): Running Jumpstarter in local mode for individual development
- [Setup Distributed Mode](#document-getting-started/usage/setup-distributed-mode): Configuring Jumpstarter for team environments with shared resources
- [Examples](#document-getting-started/usage/examples): Practical examples of Jumpstarter usage in common scenarios
- [Integration Patterns](#document-getting-started/usage/integration-patterns): Integrate Jumpstarter into your existing workflows and systems

#### Setup Local Mode[¶](#setup-local-mode "Link to this heading")

This guide shows you how to use Jumpstarter with a client and exporter running on the same host.

##### Prerequisites[¶](#prerequisites "Link to this heading")

Install [the following packages](#document-getting-started/installation/packages) in your Python environment:

- `jumpstarter-cli` - The Jumpstarter CLI for interacting with exporters
- `jumpstarter-driver-opendal` - The OpenDAL storage driver for file operations
- `jumpstarter-driver-power` - The base power driver for managing power states

These driver packages include mock implementations, enabling you to test the connection between an exporter and client without physical hardware.

##### Instructions[¶](#instructions "Link to this heading")

###### Create an Exporter Configuration[¶](#create-an-exporter-configuration "Link to this heading")

Create an exporter configuration named `example-local` to define the capabilities of your local test exporter. This configuration mirrors a regular exporter config but without the `endpoint` and `token` fields since you don’t need to connect to the controller service.

Create `example-local.yaml` in `/etc/jumpstarter/exporters` with this content:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: ExporterConfig
metadata:
  namespace: default
  name: example-local
export:
  storage:
    type: jumpstarter_driver_opendal.driver.MockStorageMux
  power:
    type: jumpstarter_driver_power.driver.MockPower
```

###### Spawn an Exporter Shell[¶](#spawn-an-exporter-shell "Link to this heading")

Interact with your local exporter using the “exporter shell” functionality in the `jmp` CLI. When you spawn a shell, Jumpstarter runs a local exporter instance in the background for the duration of your shell session.

```
$ jmp shell --exporter example-local
```

###### Exiting the Exporter Shell[¶](#exiting-the-exporter-shell "Link to this heading")

To terminate the local exporter, simply exit the shell:

```
$ exit
```

##### Next Steps[¶](#next-steps "Link to this heading")

Once you have your exporter shell running, you can start using Jumpstarter commands to interact with your hardware. To learn more about common workflow patterns and implementation examples, see [Examples](#document-getting-started/usage/examples).

#### Setup Distributed Mode[¶](#setup-distributed-mode "Link to this heading")

This guide walks you through the process of creating an exporter using the controller service, configuring drivers, and running the exporter.

Warning

The jumpstarter-controller endpoints are secured by TLS. However, in release 0.6.x, the certificates are self-signed and rotated on every restart. This means the client will not be able to verify the server certificate. To bypass this, you should use the `--insecure-tls-config` flag when creating clients and exporters. This issue will be resolved in the next release. See [issue #455](https://github.com/jumpstarter-dev/jumpstarter/issues/455) for more details. Alternatively, you can configure the ingress/route in reencrypt mode with your own key and certificate.

##### Prerequisites[¶](#prerequisites "Link to this heading")

Install [the following packages](#document-getting-started/installation/packages) in your Python environment:

- `jumpstarter-cli` - The core Jumpstarter CLI
- `jumpstarter-driver-opendal` - The OpenDAL storage driver
- `jumpstarter-driver-power` - The base power driver

These driver packages include mock implementations, enabling you to test the connection between an exporter and client without physical hardware.

You need the [service](#document-introduction/service) running in a Kubernetes cluster with admin access. For installation instructions, refer to the [installation guide](#document-getting-started/installation/service).

##### Instructions[¶](#instructions "Link to this heading")

###### Create an Exporter Configuration[¶](#create-an-exporter-configuration "Link to this heading")

Create an exporter using the controller service API. The `jmp admin` CLI provides commands to interact with the controller directly.

Run this command to create an exporter named `example-distributed` and save the configuration locally:

```
$ jmp admin create exporter example-distributed --label foo=bar --save --insecure-tls-config
```

After creating the exporter, find the new configuration file at `/etc/jumpstarter/exporters/example-distributed.yaml`. Edit the configuration using your default text editor with:

```
$ jmp config exporter edit example-distributed
```

Add the `storage` and `power` drivers under the `export` field in the configuration file. Your configuration should look like this:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: ExporterConfig
metadata:
  namespace: default
  name: example-distributed
endpoint: "<automatically filled by the controller>"
token: "<automatically filled by the controller>"
export:
  storage:
    type: jumpstarter_driver_opendal.driver.MockStorageMux
  power:
    type: jumpstarter_driver_power.driver.MockPower
```

###### Run an Exporter[¶](#run-an-exporter "Link to this heading")

Start the exporter locally using the `jmp` CLI tool:

```
$ jmp run --exporter example-distributed
```

The exporter runs until you terminate the process with or close the shell.

###### Create a Client[¶](#create-a-client "Link to this heading")

Create a client to connect to your new exporter using the `jmp admin` CLI:

The following command creates a client named “hello”, enables unsafe drivers for development purposes, and saves the configuration locally in `${HOME}/.config/jumpstarter/clients/`:

```
$ jmp admin create client hello --save --unsafe --insecure-tls-config
```

###### Spawn an Exporter Shell[¶](#spawn-an-exporter-shell "Link to this heading")

Interact with your distributed exporter using the “client shell” functionality in the `jmp` CLI. When you spawn a shell, the client attempts to acquire a lease on an exporter. Once the lease is acquired, you can interact with the exporter through your shell session.

```
$ jmp shell --client hello --selector example.com/board=foo
```

###### Exiting the Exporter Shell[¶](#exiting-the-exporter-shell "Link to this heading")

To terminate the local exporter, simply exit the shell:

```
$ exit
```

##### Next Steps[¶](#next-steps "Link to this heading")

Once you have your exporter shell running, you can start using Jumpstarter commands to interact with your hardware. To learn more about common workflow patterns and implementation examples, see [Examples](#document-getting-started/usage/examples).

#### Examples[¶](#examples "Link to this heading")

This guide provides practical examples for using Jumpstarter in both local and distributed modes. Each example demonstrates how to accomplish common tasks.

##### Starting and Exiting a Session[¶](#starting-and-exiting-a-session "Link to this heading")

Start a local exporter session:

```
$ jmp shell --exporter example-local
```

Start a distributed exporter session:

```
$ jmp shell --client hello --selector example.com/board=foo
```

When finished, simply exit the shell:

```
$ exit
```

##### Interact with the Exporter Shell[¶](#interact-with-the-exporter-shell "Link to this heading")

The exporter shell provides access to driver CLI interfaces through the magic `j` command:

```
$ jmp shell # Use appropriate --exporter or --client parameters
$ j
Usage: j [OPTIONS] COMMAND [ARGS]...

  Generic composite device

Options:
  --help  Show this message and exit.

Commands:
  power    Generic power
  storage  Generic storage mux
$ j power on
ok
$ j power off
ok
$ exit
```

When you run the `j` command in the exporter shell, you’re accessing the CLI interfaces exposed by the drivers configured in your exporter. In this example:

- `j power` - Would access the power interface from the MockPower driver
- `j storage` - Would access the storage interface from the MockStorageMux driver

Each driver can expose different commands through this interface, making it easy to interact with the mock hardware. The command structure follows `j <driver_type> <action>`, where available actions depend on the specific driver.

##### Use the Python API in a Shell[¶](#use-the-python-api-in-a-shell "Link to this heading")

The exporter shell exposes the local exporter via environment variables, enabling you to run any Python code that interacts with the client/exporter. This approach works especially well for complex operations or when a driver doesn’t provide a CLI.

###### Using Python with Jumpstarter[¶](#using-python-with-jumpstarter "Link to this heading")

Create a Python file for interacting with your exporter. This example (`example.py`) demonstrates a complete power cycle workflow:

```
import time
from jumpstarter.common.utils import env

with env() as client:
   client.power.on()
   client.power.off()
```

```
$ jmp shell # Use appropriate --exporter or --client parameters
$ python ./example.py
$ exit
```

This example demonstrates how Python interacts with the exporter:

1. The `env()` function from `jumpstarter.common.utils` automatically connects to the exporter configured in your shell environment.
2. The `with env() as client:` statement creates a client connected to your local exporter and handles connection setup and cleanup.
3. `client.power.on()` directly calls the power driver’s “on” method—the same action that `j power on` performs in the CLI.
4. `client.power.off()` directly calls the power driver’s “off” method—the same action that `j power off` performs in the CLI.

Using a Python with Jumpstarter allows you to:

- Create sequences of operations (power on → wait → power off)
- Save and reuse complex workflows
- Add logic, error handling, and conditional operations
- Import other Python libraries (like `time` in this example)
- Build sophisticated automation scripts

###### Running `pytest` in the Shell[¶](#running-pytest-in-the-shell "Link to this heading")

For multiple test cases, run a `pytest` suite using Jumpstarter’s built-in testing library as defined in `example_test.py`:

```
from jumpstarter_testing.pytest import JumpstarterTest

class MyTest(JumpstarterTest):
   def test_power_on(self, client):
      client.power.on()

   def test_power_off(self, client):
      client.power.off()
```

```
$ jmp shell # Use appropriate --exporter or --client parameters
$ pytest ./example_test.py
$ exit
```

This example demonstrates using `pytest` for structured testing with Jumpstarter:

1. The `JumpstarterTest` is a `pytest` fixture that:
   
   - Automatically establishes a connection to your exporter
   - Provides a pre-configured `client` object to each test method
   - Handles setup and teardown between tests
2. Each test method receives the `client` parameter, giving access to all driver interfaces just like in the previous examples.

Benefits of using `pytest` with Jumpstarter are:

- Organize tests into logical classes and methods
- Generate test reports with success/failure statuses
- Use `pytest`’s extensive features (parameterization, fixtures, etc.)
- Run selective tests based on names or tags

#### Integration Patterns[¶](#integration-patterns "Link to this heading")

This document outlines common integration patterns for Jumpstarter, helping you incorporate it into your development and testing workflows.

Jumpstarter integrates with various tools and platforms across the hardware development lifecycle:

- **Infrastructure**: Kubernetes, Prometheus, Grafana
- **Developer Environments**: IDE, scripts, GitHub Actions, GitLab CI, Tekton
- **Testing Frameworks**: pytest, unittest, Robot Framework

##### Infrastructure[¶](#infrastructure "Link to this heading")

###### Continuous Integration with System Testing[¶](#continuous-integration-with-system-testing "Link to this heading")

```
        ---
config:
  theme: base
  themeVariables:
    lineColor: '#3d94ff'
    primaryBorderColor: '#e5e5e5'
    primaryColor: '#f8f8f8'
    primaryTextColor: '#000'
    secondaryColor: '#f8f8f8'
    tertiaryColor: '#fff'

---
flowchart TB
    subgraph "Version Control"
        GitRepo["Git Repository"]
        Actions["GitHub/GitLab CI"]
    end

    subgraph "Jumpstarter Infrastructure"
        Controller["Controller"]
        Exporters["Exporter"]
        DUTs["Device Under Test"]
    end

    GitRepo -- "Code changes" --> Actions
    Actions -- "Request access" --> Controller
    Controller -- "Assign lease" --> Actions
    Controller -- "Connect to" --> Exporters
    Exporters -- "Control" --> DUTs
    Actions -- "Update status" --> GitRepo
    
```

This architecture integrates Jumpstarter with CI/CD pipelines to enable automated testing on real systems:

1. Code changes trigger the CI pipeline
2. The pipeline runs tests that use Jumpstarter to access systems
3. Jumpstarter’s controller manages device access and leases
4. Test results are reported back to the CI system

**CI Configuration Examples:**

GitHub GitLab

```
# .github/workflows/hardware-test.yml
jobs:
  hardware-test:
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v3
      - name: Request hardware lease
        run: |
          jmp config client use ci-client
          jmp create lease --selector project=myproject --wait 300
      - name: Run tests
        run: pytest tests/hardware_tests/
      - name: Release hardware lease
        if: always()
        run: jmp delete lease
```

```
# .gitlab-ci.yml
hardware-test:
  tags:
    - self-hosted
  script:
    - jmp config client use ci-client
    - jmp create lease --selector project=myproject --wait 300
    - pytest tests/hardware_tests/
  after_script:
    - jmp delete lease
```

###### Self-Hosted CI Runner with Attached System[¶](#self-hosted-ci-runner-with-attached-system "Link to this heading")

```
        ---
config:
  theme: base
  themeVariables:
    lineColor: '#3d94ff'
    primaryBorderColor: '#e5e5e5'
    primaryColor: '#f8f8f8'
    primaryTextColor: '#000'
    secondaryColor: '#f8f8f8'
    tertiaryColor: '#fff'

---
flowchart TB
    subgraph "Version Control"
        GitRepo["Git Repository"]
        Actions["GitHub/GitLab CI"]
    end

    subgraph "Runner"
        Runner1["Self-Hosted Runner"]
        JmpLocal["Local Mode"]
        Devices["Device Under Test"]
    end

    GitRepo -- "Code changes" --> Actions
    Actions -- "Dispatch job" --> Runner1

    Runner1 -- "Execute tests" --> JmpLocal
    JmpLocal -- "Control" --> Devices

    Runner1 -- "Report results" --> Actions
    Actions -- "Update status" --> GitRepo
    
```

This architecture leverages a self-hosted runner with directly attached system:

1. The self-hosted runner has physical devices connected directly to it
2. Jumpstarter runs in local mode on the runner, controlling the attached system
3. Code changes trigger CI jobs which are dispatched to the runner
4. Tests execute on the runner using Jumpstarter to interface with the system
5. Results are reported back to the CI system

This approach works best when:

- You need to permanently connect systems to a specific test machine
- You want to integrate system testing into existing CI/CD workflows without additional infrastructure
- You need a simple setup for initial system-in-the-loop testing

**CI Configuration Examples:**

GitHub GitLab

```
# .github/workflows/self-hosted-hw-test.yml
jobs:
  hardware-test:
    runs-on: self-hosted-hw-attached
    steps:
      - uses: actions/checkout@v3
      - name: Run Jumpstarter in local mode
        run: jmp local start --config=./.jumpstarter/local-config.yaml
      - name: Run tests
        run: pytest tests/hardware_tests/
      - name: Cleanup
        if: always()
        run: jmp local stop
```

```
# .gitlab-ci.yml
hardware-test:
  tags:
    - hw-attached
  script:
    - jmp local start --config=./.jumpstarter/local-config.yaml
    - pytest tests/hardware_tests/
  after_script:
    - jmp local stop
```

###### Cost Management and Chargeback[¶](#cost-management-and-chargeback "Link to this heading")

Organizations can implement usage-based billing for teams through a cost management layer.

```
        ---
config:
  theme: base
  themeVariables:
    lineColor: '#3d94ff'
    primaryBorderColor: '#e5e5e5'
    primaryColor: '#f8f8f8'
    primaryTextColor: '#000'
    secondaryColor: '#f8f8f8'
    tertiaryColor: '#fff'

---
flowchart LR
    subgraph "Kubernetes"
        Controller["Controller"]

        subgraph "Telemetry"
            Prometheus["Prometheus"]
            Grafana["Grafana"]
            AlertManager["AlertManager"]
        end

        subgraph "Cost Management"
            UsageTracker["Usage Tracker"]
            OpenCost["OpenCost"]
            Accounting["Chargeback System"]
        end
    end

    subgraph "Lab"
        Rack1["Exporter 1"]
        Rack2["Exporter 2"]
    end

    subgraph "Users"
        Team["Team"]
    end

    Team -- "Request access" --> Controller
    Controller -- "Assign lease" --> Team
    Controller -- "Record lease\nmetadata" --> Prometheus

    Controller -- "Connect to" --> Rack1
    Controller -- "Connect to" --> Rack2

    Rack1 -- "Report usage\nmetrics" --> Prometheus
    Rack2 -- "Report usage\nmetrics" --> Prometheus

    Prometheus -- "Store\nmetrics" --> Grafana
    Prometheus -- "Threshold\nalerts" --> AlertManager
    Prometheus -- "Usage\nmetrics" --> UsageTracker

    UsageTracker -- "Monthly billing\nreport" --> Team

    UsageTracker -- "Team resource\nusage" --> OpenCost
    OpenCost -- "Cost\nallocation" --> Accounting
    
```

This architecture implements a cost chargeback model for infrastructure resources:

1. Prometheus collects and stores all resource utilization metrics
2. Teams request resources through the controller, which records team identifiers with each lease
3. System resources export detailed utilization metrics to Prometheus:
   
   - Resource uptime and availability
   - Utilization metrics (CPU, memory, I/O)
   - Team attribution via metadata

##### Developer Environments[¶](#developer-environments "Link to this heading")

###### Traditional Developer Workflow[¶](#traditional-developer-workflow "Link to this heading")

```
        ---
config:
  theme: base
  themeVariables:
    lineColor: '#3d94ff'
    primaryBorderColor: '#e5e5e5'
    primaryColor: '#f8f8f8'
    primaryTextColor: '#000'
    secondaryColor: '#f8f8f8'
    tertiaryColor: '#fff'

---
flowchart TB
    subgraph "Workstation"
        TestCode["Test Code"]
    end

    subgraph "Local Environment"
        LocalExporter["Local Exporter"]
        DeviceOnDesk["Device Under Test"]
    end

    subgraph "Lab"
        Controller["Controller"]
        RemoteExporters["Exporter"]
        LabDevices["Device Under Test"]
    end

    TestCode --> LocalExporter
    LocalExporter --> DeviceOnDesk

    TestCode -- "Request access" --> Controller
    Controller -- "Assign lease" --> TestCode
    Controller -- "Connect to" --> RemoteExporters
    RemoteExporters --> LabDevices
    
```

This architecture supports developers working with both local systems and shared lab resources:

1. Developers write and test code in their IDE
2. For quick tests, they use the test code to access a system on their desk
3. For more complex tests, they connect to remote lab systems through the controller
4. The same test code works in both environments

See [Setup Local Mode](#document-getting-started/usage/setup-local-mode) for more information on configuring your local environment.

###### Cloud Native Developer Workflow[¶](#cloud-native-developer-workflow "Link to this heading")

```
        ---
config:
  theme: base
  themeVariables:
    lineColor: '#3d94ff'
    primaryBorderColor: '#e5e5e5'
    primaryColor: '#f8f8f8'
    primaryTextColor: '#000'
    secondaryColor: '#f8f8f8'
    tertiaryColor: '#fff'

---
flowchart TB
    subgraph "Web Browser"
        Dev["Developer"]
    end

    subgraph "Kubernetes Cluster"
        subgraph "Eclipse Che"
            Workspace["Developer Workspace"]
            TestCode["Test Code"]
            PortFwd["Port Forwarding"]
        end

        Controller["Controller"]
    end

      subgraph "Local Environment"
          LocalExporter["Local Exporter"]
          DeviceOnDesk["Device Under Test"]
      end

      subgraph "Lab"
          RemoteExporters["Exporter"]
          LabDevices["Device Under Test"]
      end

    Dev -- "Access via browser" --> Workspace
    Workspace -- "Contains" --> TestCode

    TestCode -- "Local system access" --> PortFwd
    PortFwd -- "Forward connection" --> LocalExporter
    LocalExporter -- "Control" --> DeviceOnDesk

    TestCode -- "Request access" --> Controller
    Controller -- "Assign lease" --> TestCode
    Controller -- "Connect to" --> RemoteExporters
    RemoteExporters -- "Control" --> LabDevices
    
```

This architecture provides a cloud-native development experience while maintaining flexibility to work with both local and remote systems:

1. Developers access a containerized development environment through a web browser using Eclipse Che
2. The development workspace contains all necessary tools, dependencies, and test code
3. For quick iterations with locally connected systems:
   
   - Port forwarding enables the cloud workspace to communicate with systems connected to the developer’s machine
   - The local Jumpstarter exporter manages the device directly
4. For access to shared lab resources:
   
   - The same test code can request access to remote devices through the controller
   - The controller manages leases and routes connections through the standard infrastructure

Key benefits of this approach:

- **Consistent Development Environment**: Standardized, reproducible workspaces for all team members
- **Flexibility**: Seamless transition between local and remote system testing
- **Collaboration**: Web-based IDE enables real-time collaboration and knowledge sharing
- **Scalability**: Easy onboarding of new team members with zero local configuration
- **System Flexibility**: Enables a hybrid approach where developers can test locally first, then validate on shared lab systems

This workflow eliminates the distinction between local and cloud development while providing the best of both worlds for system testing.

See [Setup Distributed Mode](#document-getting-started/usage/setup-distributed-mode) for more details on configuring your distributed environment.

##### Testing Frameworks[¶](#testing-frameworks "Link to this heading")

###### pytest Integration[¶](#pytest-integration "Link to this heading")

Jumpstarter integrates with pytest through the `jumpstarter-testing` package:

```
from jumpstarter_testing.pytest import JumpstarterTest

class TestMyDevice(JumpstarterTest):
    # Optional: specify which exporter to use based on labels
    exporter_selector = "vendor=acme,model=widget-v2"

    def test_power_cycle(self):
        # Access the device driver through the provided client
        self.client.power.on()
        assert self.client.serial.read_until("boot complete") is not None
        self.client.power.off()
```

###### Robot Framework Integration[¶](#robot-framework-integration "Link to this heading")

For teams using Robot Framework, Jumpstarter drivers can be exposed as keywords:

```
*** Settings ***
Library    JumpstarterLibrary

*** Test Cases ***
Device Boot Test
    Connect To Exporter    selector=vendor=acme,model=widget-v2
    Power On
    ${output}=    Read Serial Until    boot complete
    Should Not Be Empty    ${output}
    Power Off
```

##### Recommended Practices[¶](#recommended-practices "Link to this heading")

###### Labeling Strategy[¶](#labeling-strategy "Link to this heading")

Develop a consistent labeling strategy for your exporters to make device selection straightforward:

- **System Properties**: `arch=arm64`, `cpu=cortex-a53`
- **Organization**: `team=platform`, `project=widget`
- **Capabilities**: `has-video=true`, `has-can=true`
- **Environment**: `env=dev`, `env=production`

###### Resource Management[¶](#resource-management "Link to this heading")

Implement these practices to ensure efficient use of shared systems:

- Set appropriate lease timeouts to prevent orphaned resources
- Use CI systems’ concurrency controls to manage test parallelism
- Implement monitoring and alerting for device availability
- Create “pools” of identical devices to improve scalability

###### Security Considerations[¶](#security-considerations "Link to this heading")

When deploying Jumpstarter in a multi-user environment:

- Use role-based access control to limit which users can access which devices
- Restrict driver access to prevent untrusted code execution
- Isolate the Jumpstarter network from production systems
- Rotate JWT tokens regularly for enhanced security

## Contributing[¶](#contributing "Link to this heading")

Thank you for your interest in contributing to Jumpstarter, we are an open community and we welcome contributions.

### Getting Help[¶](#getting-help "Link to this heading")

- **Matrix**: [Community](index.html#jumpstarter:matrix.org)
- **GitHub**: [Issues](https://github.com/jumpstarter-dev/jumpstarter/issues)
- **Documentation**: [Website](https://jumpstarter.dev/)
- **Weekly Meeting**: [Google Meet](https://meet.google.com/gzd-hhbd-hpu)
- **Etherpad**: [Docs](https://etherpad.jumpstarter.dev/pad-lister)

### Getting Started[¶](#getting-started "Link to this heading")

0. Get familiar with [Jumpstarter Internals](#document-contributing/internals)
1. Follow our [dev setup guide](#document-contributing/development-environment)
2. Make changes on a new branch
3. Test your changes thoroughly
4. Submit a pull request

If you have questions, reach out in our Matrix chat or open an issue on GitHub.

### Contribution Guidelines[¶](#contribution-guidelines "Link to this heading")

#### Making Changes[¶](#making-changes "Link to this heading")

- Focus on a single issue.
- Follow code style (validate with `make lint`, fix with `make lint-fix`)
- Perform static type checking with (`make ty-pkg-${package_name}`)
- Add tests and update documentation. New drivers/features need tests and docs.
- Verify all tests pass (`make test-pkg-${package_name}` or `make test`)

#### Commit Messages[¶](#commit-messages "Link to this heading")

- Use clear, descriptive messages
- Reference issue numbers when applicable
- Follow conventional commit format when possible

#### Pull Requests[¶](#pull-requests "Link to this heading")

- Provide a clear description
- Link to relevant issues
- Ensure all tests pass

### Types of Contributions[¶](#types-of-contributions "Link to this heading")

#### Code Contributions[¶](#code-contributions "Link to this heading")

We welcome bug fixes, features, and improvements to the core codebase.

#### Contributing Drivers[¶](#contributing-drivers "Link to this heading")

To create a new driver scaffold:

```
$ ./__templates__/create_driver.sh driver_package DriverClass "Your Name" "your.email@example.com"
```

For private drivers, consider forking our [jumpstarter-driver-template](https://github.com/jumpstarter-dev/jumpstarter-driver-template).

Test your driver: `make pkg-test-${package_name}`

#### Contributing Documentation[¶](#contributing-documentation "Link to this heading")

Jumpstarter uses Sphinx with Markdown. Build and preview locally:

```
$ make docs-serve
```

Documentation recommended practices:

- Use clear, concise language
- Include practical examples
- Break up text with headers, lists, and code blocks
- Target both beginners and advanced users

##### Development Environment[¶](#development-environment "Link to this heading")

You can use [devspaces](https://github.com/jumpstarter-dev/jumpstarter/blob/main/.devfile.yaml), [devcontainers](https://github.com/jumpstarter-dev/jumpstarter/tree/main/.devcontainer), or your favorite OS/distro to develop Jumpstarter, however the following examples are for Fedora 42.

Jumpstarter is programmed in Python and Go, the Jumpstarter controller is written in Go, while the core and drivers are written in Python.

###### Python Environment[¶](#python-environment "Link to this heading")

The Jumpstarter core and drivers live in the [jumpstarter](https://github.com/jumpstarter-dev/jumpstarter) repository.

We use [uv](https://docs.astral.sh/uv/) as our python package and project manager, and `make` as our build interface.

To install the basic set of dependencies, run the following commands:

```
$ sudo dnf install -y python-devel g++ make git uv qemu qemu-user-static
```

Then you can clone the project and build the virtual environment with:

```
$ git clone https://github.com/jumpstarter-dev/jumpstarter.git
$ cd jumpstarter
$ make sync
```

At this point you can run any of the jumpstarter commands prefixing them with `uv run`:

```
$ uv run jmp
```

###### Running the Tests[¶](#running-the-tests "Link to this heading")

To run the tests, you can use the `make` command:

```
$ make test
```

You can also run specific tests with:

```
$ make test-pkg-${package_name}
```

###### Go Environment[¶](#go-environment "Link to this heading")

The Jumpstarter controller lives in the [jumpstarter-controller](https://github.com/jumpstarter-dev/jumpstarter-controller) repository.

To install the basic set of dependencies, run the following commands:

```
$ sudo dnf install -y git make golang kubectl
```

Then you can clone the project and build the project with:

```
$ git clone https://github.com/jumpstarter-dev/jumpstarter-controller.git
$ cd jumpstarter-controller
$ make build
```

At this point you can deploy the controller in a kubernetes cluster in docker (`kind`) with:

```
$ CONTAINER_TOOL=podman make deploy
```

And you can cleanup and stop the controller/cluster with:

```
$ CONTAINER_TOOL=podman make clean
```

###### Running the Tests[¶](#id1 "Link to this heading")

To run the tests, you can use the `make` command:

```
$ make test
```

##### Internals[¶](#internals "Link to this heading")

###### Architecture[¶](#architecture "Link to this heading")

Jumpstarter consists of primarily three components, the control plane (`Controller` and `Router`) running inside a kubernetes cluster, the `Exporter` running on dedicated `Exporter Hosts` or developer machines (for local development workflow), and the `Client` interacting with the `Exporter`.

The `Controller` handles inventory/lease management and access control, and stores its states as kubernetes CRDs. The `Router` provides a rendezvous point for clients to connect to exporters not on the local network. THe `Exporter` interacts with the `Device Under Test` with a set of `Drivers`, and exposes the methods provided by the `Drivers` over the network. The `Client` connects to the `Exporter` either directly, or over the `Router`, and calls the methods provided by the `Drivers` to perform actions on the `Device Under Test`.

![Architecture](_images/architecture.png)

###### RPC[¶](#rpc "Link to this heading")

Jumpstarter in its essence, is a RPC framework for `Clients` to call methods provided by `Drivers`. `Drivers` can expose three styles of RPCs, `Unary`, `Server streaming` and `Bidirectional streaming`, which are implemented with their counterparts in `gRPC`, see [RPC life cycle](https://grpc.io/docs/what-is-grpc/core-concepts/#rpc-life-cycle) for an in depth introduction to these RPC types.

![RPC](_images/rpc.png)

On top of `Bidirectional streaming` RPC, Jumpstarter also implements a generic byte stream interface, similar to TCP, for tunneling existing protocol (e.g. SSH) over Jumpstarter.

###### Router[¶](#router "Link to this heading")

The Jumpstarter `Router` is just like ngrok or Cloudflare Tunnel, it allows for the `Client` to connect to `Exporters` without public IP addresses or behind NATs/firewalls, by tunneling a byte stream over Bidirectional streaming gRPC.

![Router](_images/router.png)

## Glossary[¶](#glossary "Link to this heading")

### Acronyms[¶](#acronyms "Link to this heading")

- `DUT`: Device Under Test
- `CRD`: Custom Resource Definition
- `CI/CD`: Continuous Integration/Continuous Deployment
- `gRPC`: Google Remote Procedure Call
- `JWT`: JSON Web Token
- `KVM`: Keyboard, Video, Mouse

### Entities[¶](#entities "Link to this heading")

- `exporter`: A Linux service that exports the interfaces to the DUTs. An exporter connects directly to a Jumpstarter server or directly to a client.
- `client`: A developer or a CI/CD pipeline that connects to the Jumpstarter server and leases exporters. The client can run tests on the leased resources.
- `controller`: The central service that authenticates and connects the exporters and clients, manages leases, and provides an inventory of available exporters and clients.
- `router`: A service used by the controller to route messages between clients and exporters through a gRPC tunnel, enabling remote access to exported interfaces.
- `host`: A system running the exporter service, typically a low-cost test system such as a single board computer with sufficient interfaces to connect to hardware.

### Concepts[¶](#concepts "Link to this heading")

- `device`: A device that is exposed on an exporter. The exporter enumerates these devices and makes them available for use in tests. Examples of resources include:
  
  - Network interface
  - Serial port
  - GPIO pin
  - Storage device (USB Muxer, SD-Wire, etc.)
  - CAN bus interface
- `lease`: A time-limited reservation of an exporter. A lease is created by a client and allows the client to use the exporter resources for a limited time. Leases ensure exclusive access to specific devices/exporters.
- `adapter`: A component that transforms connections exposed by drivers into different forms or interfaces. Adapters take a driver client as input and provide alternative ways to interact with the underlying connection, such as port forwarding, VNC access, or terminal emulation.
- `interface class`: An abstract base class that defines the contract for driver implementations. It specifies the required methods that must be implemented by driver classes and provides the client class path through the `client()` class method.
- `driver class`: A class that implements an interface and inherits from the `Driver` base class. It uses the `@export` decorator to expose methods that can be called remotely by clients.
- `driver client class`: The driver client class that is used directly by end users. It interacts with the `driver class` remotely via remote procedure call to invoke exported methods, which in turn interact with the exporter resources.
- `driver`: The term for both the `driver class` and the corresponding `driver client class`, not to be confused with `Driver`, the base class of all `driver classes`. Drivers in the main `jumpstarter` repository are called `in-tree drivers`, otherwise they are called `out-of-tree drivers`. Drivers implementing predefined interfaces are called `standard drivers`, otherwise they are called `custom drivers`.
- `composite driver`: A driver that combines multiple lower-level drivers to create higher-level abstractions or specialized workflows, organized in a tree structure to represent complex device configurations.
- `local mode`: An operation mode where clients communicate directly with exporters running on the same machine or through direct network connections, ideal for individual developers working directly with accessible hardware or virtual devices.
- `distributed mode`: An operation mode that enables multiple teams to securely share hardware resources across a network using a Kubernetes-based controller to coordinate access to exporters and manage leases.
- `stream`: A continuous data exchange channel established by drivers for communications like serial connections or video streaming, enabling real-time interaction with both physical and virtual interfaces across the network.
- `message`: Commands sent from driver clients to driver implementations, allowing the client to trigger actions or retrieve information from the device.

## Reference[¶](#reference "Link to this heading")

This section provides reference documentation for Jumpstarter. The documentation covers:

- [API Pages](#document-reference/man-pages/index): Command-line tools and utilities documentation
- [Packages](#document-reference/package-apis/index): API documentation for Jumpstarter packages and components

These references are useful for developers working with Jumpstarter.

### MAN Pages[¶](#man-pages "Link to this heading")

This section provides reference documentation for Jumpstarter’s command-line interfaces. The documentation covers:

- [`jmp`](#document-reference/man-pages/jmp): Main command-line interface for Jumpstarter
- [`j`](#document-reference/man-pages/j): Shorthand utility for quick interactions with Jumpstarter

These references support both local and distributed deployment modes of Jumpstarter.

#### jmp[¶](#jmp "Link to this heading")

The Jumpstarter CLI

```
jmp [OPTIONS] COMMAND [ARGS]...
```

Options

--log-level &lt;log\_level&gt;[¶](#cmdoption-jmp-log-level "Link to this definition")

Set the log level

Options:

DEBUG | INFO | WARNING | ERROR | CRITICAL

##### admin[¶](#jmp-admin "Link to this heading")

Jumpstarter Kubernetes cluster admin CLI tool

```
jmp admin [OPTIONS] COMMAND [ARGS]...
```

Options

--log-level &lt;log\_level&gt;[¶](#cmdoption-jmp-admin-log-level "Link to this definition")

Set the log level

Options:

DEBUG | INFO | WARNING | ERROR | CRITICAL

###### create[¶](#jmp-admin-create "Link to this heading")

Create Jumpstarter Kubernetes objects

```
jmp admin create [OPTIONS] COMMAND [ARGS]...
```

###### client[¶](#jmp-admin-create-client "Link to this heading")

Create a client object in the Kubernetes cluster

```
jmp admin create client [OPTIONS] [NAME]
```

Options

-s, --save[¶](#cmdoption-jmp-admin-create-client-s "Link to this definition")

Save the config file for the created client.

-a, --allow &lt;allow&gt;[¶](#cmdoption-jmp-admin-create-client-a "Link to this definition")

A comma-separated list of driver client packages to load.

--unsafe[¶](#cmdoption-jmp-admin-create-client-unsafe "Link to this definition")

Should all driver client packages be allowed to load (UNSAFE!).

--out &lt;out&gt;[¶](#cmdoption-jmp-admin-create-client-out "Link to this definition")

Specify an output file for the client config.

-n, --namespace &lt;namespace&gt;[¶](#cmdoption-jmp-admin-create-client-n "Link to this definition")

Kubernetes namespace to use

-l, --label &lt;labels&gt;[¶](#cmdoption-jmp-admin-create-client-l "Link to this definition")

Labels to set on resource, can be set multiple times

--kubeconfig &lt;kubeconfig&gt;[¶](#cmdoption-jmp-admin-create-client-kubeconfig "Link to this definition")

path to the kubeconfig file

--context &lt;context&gt;[¶](#cmdoption-jmp-admin-create-client-context "Link to this definition")

Kubernetes context to use

--insecure-tls-config[¶](#cmdoption-jmp-admin-create-client-insecure-tls-config "Link to this definition")

Disable endpoint TLS verification. This is insecure and should only be used for testing purposes

--oidc-username &lt;oidc\_username&gt;[¶](#cmdoption-jmp-admin-create-client-oidc-username "Link to this definition")

OIDC username

--nointeractive[¶](#cmdoption-jmp-admin-create-client-nointeractive "Link to this definition")

Disable interactive prompts (for use in scripts).

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-admin-create-client-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

Arguments

NAME[¶](#cmdoption-jmp-admin-create-client-arg-NAME "Link to this definition")

Optional argument

###### exporter[¶](#jmp-admin-create-exporter "Link to this heading")

Create an exporter object in the Kubernetes cluster

```
jmp admin create exporter [OPTIONS] [NAME]
```

Options

-s, --save[¶](#cmdoption-jmp-admin-create-exporter-s "Link to this definition")

Save the config file for the created exporter.

--out &lt;out&gt;[¶](#cmdoption-jmp-admin-create-exporter-out "Link to this definition")

Specify an output file for the exporter config.

-n, --namespace &lt;namespace&gt;[¶](#cmdoption-jmp-admin-create-exporter-n "Link to this definition")

Kubernetes namespace to use

-l, --label &lt;labels&gt;[¶](#cmdoption-jmp-admin-create-exporter-l "Link to this definition")

**Required** Labels to set on resource, can be set multiple times

--kubeconfig &lt;kubeconfig&gt;[¶](#cmdoption-jmp-admin-create-exporter-kubeconfig "Link to this definition")

path to the kubeconfig file

--context &lt;context&gt;[¶](#cmdoption-jmp-admin-create-exporter-context "Link to this definition")

Kubernetes context to use

--insecure-tls-config[¶](#cmdoption-jmp-admin-create-exporter-insecure-tls-config "Link to this definition")

Disable endpoint TLS verification. This is insecure and should only be used for testing purposes

--oidc-username &lt;oidc\_username&gt;[¶](#cmdoption-jmp-admin-create-exporter-oidc-username "Link to this definition")

OIDC username

--nointeractive[¶](#cmdoption-jmp-admin-create-exporter-nointeractive "Link to this definition")

Disable interactive prompts (for use in scripts).

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-admin-create-exporter-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

Arguments

NAME[¶](#cmdoption-jmp-admin-create-exporter-arg-NAME "Link to this definition")

Optional argument

###### delete[¶](#jmp-admin-delete "Link to this heading")

Create Jumpstarter Kubernetes objects

```
jmp admin delete [OPTIONS] COMMAND [ARGS]...
```

###### client[¶](#jmp-admin-delete-client "Link to this heading")

Delete a client object in the Kubernetes cluster

```
jmp admin delete client [OPTIONS] [NAME]
```

Options

-d, --delete[¶](#cmdoption-jmp-admin-delete-client-d "Link to this definition")

Delete the config file for the client.

-n, --namespace &lt;namespace&gt;[¶](#cmdoption-jmp-admin-delete-client-n "Link to this definition")

Kubernetes namespace to use

--kubeconfig &lt;kubeconfig&gt;[¶](#cmdoption-jmp-admin-delete-client-kubeconfig "Link to this definition")

path to the kubeconfig file

--context &lt;context&gt;[¶](#cmdoption-jmp-admin-delete-client-context "Link to this definition")

Kubernetes context to use

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-admin-delete-client-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

name

--nointeractive[¶](#cmdoption-jmp-admin-delete-client-nointeractive "Link to this definition")

Disable interactive prompts (for use in scripts).

Arguments

NAME[¶](#cmdoption-jmp-admin-delete-client-arg-NAME "Link to this definition")

Optional argument

###### exporter[¶](#jmp-admin-delete-exporter "Link to this heading")

Delete an exporter object in the Kubernetes cluster

```
jmp admin delete exporter [OPTIONS] [NAME]
```

Options

-d, --delete[¶](#cmdoption-jmp-admin-delete-exporter-d "Link to this definition")

Delete the config file for the exporter.

-n, --namespace &lt;namespace&gt;[¶](#cmdoption-jmp-admin-delete-exporter-n "Link to this definition")

Kubernetes namespace to use

--kubeconfig &lt;kubeconfig&gt;[¶](#cmdoption-jmp-admin-delete-exporter-kubeconfig "Link to this definition")

path to the kubeconfig file

--context &lt;context&gt;[¶](#cmdoption-jmp-admin-delete-exporter-context "Link to this definition")

Kubernetes context to use

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-admin-delete-exporter-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

name

--nointeractive[¶](#cmdoption-jmp-admin-delete-exporter-nointeractive "Link to this definition")

Disable interactive prompts (for use in scripts).

Arguments

NAME[¶](#cmdoption-jmp-admin-delete-exporter-arg-NAME "Link to this definition")

Optional argument

###### get[¶](#jmp-admin-get "Link to this heading")

Get Jumpstarter Kubernetes objects

```
jmp admin get [OPTIONS] COMMAND [ARGS]...
```

###### client[¶](#jmp-admin-get-client "Link to this heading")

Get the client objects in a Kubernetes cluster

```
jmp admin get client [OPTIONS] [NAME]
```

Options

-n, --namespace &lt;namespace&gt;[¶](#cmdoption-jmp-admin-get-client-n "Link to this definition")

Kubernetes namespace to use

--kubeconfig &lt;kubeconfig&gt;[¶](#cmdoption-jmp-admin-get-client-kubeconfig "Link to this definition")

path to the kubeconfig file

--context &lt;context&gt;[¶](#cmdoption-jmp-admin-get-client-context "Link to this definition")

Kubernetes context to use

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-admin-get-client-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

Arguments

NAME[¶](#cmdoption-jmp-admin-get-client-arg-NAME "Link to this definition")

Optional argument

###### exporter[¶](#jmp-admin-get-exporter "Link to this heading")

Get the exporter objects in a Kubernetes cluster

```
jmp admin get exporter [OPTIONS] [NAME]
```

Options

-n, --namespace &lt;namespace&gt;[¶](#cmdoption-jmp-admin-get-exporter-n "Link to this definition")

Kubernetes namespace to use

--kubeconfig &lt;kubeconfig&gt;[¶](#cmdoption-jmp-admin-get-exporter-kubeconfig "Link to this definition")

path to the kubeconfig file

--context &lt;context&gt;[¶](#cmdoption-jmp-admin-get-exporter-context "Link to this definition")

Kubernetes context to use

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-admin-get-exporter-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

-d, --devices[¶](#cmdoption-jmp-admin-get-exporter-d "Link to this definition")

Display the devices hosted by the exporter(s)

Arguments

NAME[¶](#cmdoption-jmp-admin-get-exporter-arg-NAME "Link to this definition")

Optional argument

###### lease[¶](#jmp-admin-get-lease "Link to this heading")

Get the lease objects in a Kubernetes cluster

```
jmp admin get lease [OPTIONS] [NAME]
```

Options

-n, --namespace &lt;namespace&gt;[¶](#cmdoption-jmp-admin-get-lease-n "Link to this definition")

Kubernetes namespace to use

--kubeconfig &lt;kubeconfig&gt;[¶](#cmdoption-jmp-admin-get-lease-kubeconfig "Link to this definition")

path to the kubeconfig file

--context &lt;context&gt;[¶](#cmdoption-jmp-admin-get-lease-context "Link to this definition")

Kubernetes context to use

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-admin-get-lease-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

Arguments

NAME[¶](#cmdoption-jmp-admin-get-lease-arg-NAME "Link to this definition")

Optional argument

###### import[¶](#jmp-admin-import "Link to this heading")

Import configs from a Kubernetes cluster

```
jmp admin import [OPTIONS] COMMAND [ARGS]...
```

###### client[¶](#jmp-admin-import-client "Link to this heading")

Import a client config from a Kubernetes cluster

```
jmp admin import client [OPTIONS] NAME
```

Options

--out &lt;out&gt;[¶](#cmdoption-jmp-admin-import-client-out "Link to this definition")

Specify an output file for the client config.

-a, --allow &lt;allow&gt;[¶](#cmdoption-jmp-admin-import-client-a "Link to this definition")

A comma-separated list of driver client packages to load.

--unsafe[¶](#cmdoption-jmp-admin-import-client-unsafe "Link to this definition")

Should all driver client packages be allowed to load (UNSAFE!).

-n, --namespace &lt;namespace&gt;[¶](#cmdoption-jmp-admin-import-client-n "Link to this definition")

Kubernetes namespace to use

--kubeconfig &lt;kubeconfig&gt;[¶](#cmdoption-jmp-admin-import-client-kubeconfig "Link to this definition")

path to the kubeconfig file

--context &lt;context&gt;[¶](#cmdoption-jmp-admin-import-client-context "Link to this definition")

Kubernetes context to use

--insecure-tls-config[¶](#cmdoption-jmp-admin-import-client-insecure-tls-config "Link to this definition")

Disable endpoint TLS verification. This is insecure and should only be used for testing purposes

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-admin-import-client-o "Link to this definition")

Output mode. Use “-o path” for shorter output (file/path).

Options:

path

--nointeractive[¶](#cmdoption-jmp-admin-import-client-nointeractive "Link to this definition")

Disable interactive prompts (for use in scripts).

Arguments

NAME[¶](#cmdoption-jmp-admin-import-client-arg-NAME "Link to this definition")

Required argument

###### exporter[¶](#jmp-admin-import-exporter "Link to this heading")

Import an exporter config from a Kubernetes cluster

```
jmp admin import exporter [OPTIONS] [NAME]
```

Options

--out &lt;out&gt;[¶](#cmdoption-jmp-admin-import-exporter-out "Link to this definition")

Specify an output file for the exporter config.

-n, --namespace &lt;namespace&gt;[¶](#cmdoption-jmp-admin-import-exporter-n "Link to this definition")

Kubernetes namespace to use

--kubeconfig &lt;kubeconfig&gt;[¶](#cmdoption-jmp-admin-import-exporter-kubeconfig "Link to this definition")

path to the kubeconfig file

--context &lt;context&gt;[¶](#cmdoption-jmp-admin-import-exporter-context "Link to this definition")

Kubernetes context to use

--insecure-tls-config[¶](#cmdoption-jmp-admin-import-exporter-insecure-tls-config "Link to this definition")

Disable endpoint TLS verification. This is insecure and should only be used for testing purposes

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-admin-import-exporter-o "Link to this definition")

Output mode. Use “-o path” for shorter output (file/path).

Options:

path

--nointeractive[¶](#cmdoption-jmp-admin-import-exporter-nointeractive "Link to this definition")

Disable interactive prompts (for use in scripts).

Arguments

NAME[¶](#cmdoption-jmp-admin-import-exporter-arg-NAME "Link to this definition")

Optional argument

###### install[¶](#jmp-admin-install "Link to this heading")

Install the Jumpstarter service in a Kubernetes cluster

```
jmp admin install [OPTIONS]
```

Options

--helm &lt;helm&gt;[¶](#cmdoption-jmp-admin-install-helm "Link to this definition")

Path or name of a helm executable

--name &lt;name&gt;[¶](#cmdoption-jmp-admin-install-name "Link to this definition")

The name of the chart installation

-c, --chart &lt;chart&gt;[¶](#cmdoption-jmp-admin-install-c "Link to this definition")

The URL of a Jumpstarter helm chart to install

-n, --namespace &lt;namespace&gt;[¶](#cmdoption-jmp-admin-install-n "Link to this definition")

Namespace to install Jumpstarter components in

-i, --ip &lt;ip&gt;[¶](#cmdoption-jmp-admin-install-i "Link to this definition")

IP address of your host machine

-b, --basedomain &lt;basedomain&gt;[¶](#cmdoption-jmp-admin-install-b "Link to this definition")

Base domain of the Jumpstarter service

-g, --grpc-endpoint &lt;grpc\_endpoint&gt;[¶](#cmdoption-jmp-admin-install-g "Link to this definition")

The gRPC endpoint to use for the Jumpstarter API

-r, --router-endpoint &lt;router\_endpoint&gt;[¶](#cmdoption-jmp-admin-install-r "Link to this definition")

The gRPC endpoint to use for the router

--nodeport[¶](#cmdoption-jmp-admin-install-nodeport "Link to this definition")

Use Nodeport routing (recommended)

--ingress[¶](#cmdoption-jmp-admin-install-ingress "Link to this definition")

Use a Kubernetes ingress

--route[¶](#cmdoption-jmp-admin-install-route "Link to this definition")

Use an OpenShift route

-v, --version &lt;version&gt;[¶](#cmdoption-jmp-admin-install-v "Link to this definition")

The version of the service to install

--kubeconfig &lt;kubeconfig&gt;[¶](#cmdoption-jmp-admin-install-kubeconfig "Link to this definition")

path to the kubeconfig file

--context &lt;context&gt;[¶](#cmdoption-jmp-admin-install-context "Link to this definition")

Kubernetes context to use

###### version[¶](#jmp-admin-version "Link to this heading")

Get the current Jumpstarter version

```
jmp admin version [OPTIONS]
```

Options

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-admin-version-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

##### config[¶](#jmp-config "Link to this heading")

```
jmp config [OPTIONS] COMMAND [ARGS]...
```

###### client[¶](#jmp-config-client "Link to this heading")

Modify jumpstarter client config files

```
jmp config client [OPTIONS] COMMAND [ARGS]...
```

###### create[¶](#jmp-config-client-create "Link to this heading")

Create a Jumpstarter client configuration.

```
jmp config client create [OPTIONS] ALIAS
```

Options

--out &lt;out&gt;[¶](#cmdoption-jmp-config-client-create-out "Link to this definition")

Specify an output file for the client config.

--namespace &lt;namespace&gt;[¶](#cmdoption-jmp-config-client-create-namespace "Link to this definition")

Enter the Jumpstarter client namespace.

--name &lt;name&gt;[¶](#cmdoption-jmp-config-client-create-name "Link to this definition")

Enter the Jumpstarter client name.

-e, --endpoint &lt;endpoint&gt;[¶](#cmdoption-jmp-config-client-create-e "Link to this definition")

Enter the Jumpstarter service endpoint.

-t, --token &lt;token&gt;[¶](#cmdoption-jmp-config-client-create-t "Link to this definition")

A valid Jumpstarter auth token generated by the Jumpstarter service.

-a, --allow &lt;allow&gt;[¶](#cmdoption-jmp-config-client-create-a "Link to this definition")

A comma-separated list of driver client packages to load.

--unsafe[¶](#cmdoption-jmp-config-client-create-unsafe "Link to this definition")

Should all driver client packages be allowed to load (UNSAFE!).

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-config-client-create-o "Link to this definition")

Output mode. Use “-o path” for shorter output (file/path).

Options:

path

Arguments

ALIAS[¶](#cmdoption-jmp-config-client-create-arg-ALIAS "Link to this definition")

Required argument

###### delete[¶](#jmp-config-client-delete "Link to this heading")

Delete a Jumpstarter client configuration.

```
jmp config client delete [OPTIONS] NAME
```

Options

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-config-client-delete-o "Link to this definition")

Output mode. Use “-o path” for shorter output (file/path).

Options:

path

Arguments

NAME[¶](#cmdoption-jmp-config-client-delete-arg-NAME "Link to this definition")

Required argument

###### list[¶](#jmp-config-client-list "Link to this heading")

List available client configurations.

```
jmp config client list [OPTIONS]
```

Options

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-config-client-list-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

###### use[¶](#jmp-config-client-use "Link to this heading")

Select the current Jumpstarter client configuration to use.

```
jmp config client use [OPTIONS] NAME
```

Options

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-config-client-use-o "Link to this definition")

Output mode. Use “-o path” for shorter output (file/path).

Options:

path

Arguments

NAME[¶](#cmdoption-jmp-config-client-use-arg-NAME "Link to this definition")

Required argument

###### exporter[¶](#jmp-config-exporter "Link to this heading")

Modify jumpstarter exporter config files

```
jmp config exporter [OPTIONS] COMMAND [ARGS]...
```

###### create[¶](#jmp-config-exporter-create "Link to this heading")

Create an exporter config.

```
jmp config exporter create [OPTIONS] [ALIAS]
```

Options

--namespace &lt;namespace&gt;[¶](#cmdoption-jmp-config-exporter-create-namespace "Link to this definition")

--name &lt;name&gt;[¶](#cmdoption-jmp-config-exporter-create-name "Link to this definition")

--endpoint &lt;endpoint&gt;[¶](#cmdoption-jmp-config-exporter-create-endpoint "Link to this definition")

--token &lt;token&gt;[¶](#cmdoption-jmp-config-exporter-create-token "Link to this definition")

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-config-exporter-create-o "Link to this definition")

Output mode. Use “-o path” for shorter output (file/path).

Options:

path

Arguments

ALIAS[¶](#cmdoption-jmp-config-exporter-create-arg-ALIAS "Link to this definition")

Optional argument

###### delete[¶](#jmp-config-exporter-delete "Link to this heading")

Delete an exporter config.

```
jmp config exporter delete [OPTIONS] [ALIAS]
```

Options

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-config-exporter-delete-o "Link to this definition")

Output mode. Use “-o path” for shorter output (file/path).

Options:

path

Arguments

ALIAS[¶](#cmdoption-jmp-config-exporter-delete-arg-ALIAS "Link to this definition")

Optional argument

###### edit[¶](#jmp-config-exporter-edit "Link to this heading")

Edit an exporter config.

```
jmp config exporter edit [OPTIONS] [ALIAS]
```

Arguments

ALIAS[¶](#cmdoption-jmp-config-exporter-edit-arg-ALIAS "Link to this definition")

Optional argument

###### list[¶](#jmp-config-exporter-list "Link to this heading")

List exporter configs.

```
jmp config exporter list [OPTIONS]
```

Options

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-config-exporter-list-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

##### create[¶](#jmp-create "Link to this heading")

Create a resource

```
jmp create [OPTIONS] COMMAND [ARGS]...
```

###### lease[¶](#jmp-create-lease "Link to this heading")

Create a lease

Request an exporter lease from the jumpstarter controller.

The result of this command will be a lease ID that can be used to connect to the remote exporter.

This is useful for multi-step workflows where you want to hold a lease for a specific exporter while performing multiple operations, or for CI environments where one step will request the lease and other steps will perform operations on the leased exporter.

Example:

```
$ JMP_LEASE=$(jmp create lease -l foo=bar --duration 1d --output name)
$ jmp shell
$$ j --help
$$ exit
$ jmp delete lease "${JMP_LEASE}"
```

```
jmp create lease [OPTIONS]
```

Options

--client-config &lt;client\_config&gt;[¶](#cmdoption-jmp-create-lease-client-config "Link to this definition")

Path to client config

--client &lt;client&gt;[¶](#cmdoption-jmp-create-lease-client "Link to this definition")

Alias of client config

-l, --selector &lt;selector&gt;[¶](#cmdoption-jmp-create-lease-l "Link to this definition")

Selector (label query) to filter on, supports ‘=’, ‘==’, and ‘!=’ (e.g. -l key1=value1,key2=value2). Matching objects must satisfy all of the specified label constraints.

--duration &lt;duration&gt;[¶](#cmdoption-jmp-create-lease-duration "Link to this definition")

**Required** Accepted duration formats:

PnYnMnDTnHnMnS - ISO 8601 duration format

HH:MM:SS - time in hours, minutes, seconds

D days, HH:MM:SS - time prefixed by X days

D d, HH:MM:SS - time prefixed by X d

See [https://docs.rs/speedate/latest/speedate/](https://docs.rs/speedate/latest/speedate/) for details

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-create-lease-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

##### delete[¶](#jmp-delete "Link to this heading")

Delete resources

```
jmp delete [OPTIONS] COMMAND [ARGS]...
```

###### leases[¶](#jmp-delete-leases "Link to this heading")

Delete leases

```
jmp delete leases [OPTIONS] [NAME]
```

Options

--client-config &lt;client\_config&gt;[¶](#cmdoption-jmp-delete-leases-client-config "Link to this definition")

Path to client config

--client &lt;client&gt;[¶](#cmdoption-jmp-delete-leases-client "Link to this definition")

Alias of client config

-l, --selector &lt;selector&gt;[¶](#cmdoption-jmp-delete-leases-l "Link to this definition")

Selector (label query) to filter on, supports ‘=’, ‘==’, and ‘!=’ (e.g. -l key1=value1,key2=value2). Matching objects must satisfy all of the specified label constraints.

--all[¶](#cmdoption-jmp-delete-leases-all "Link to this definition")

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-delete-leases-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

name

Arguments

NAME[¶](#cmdoption-jmp-delete-leases-arg-NAME "Link to this definition")

Optional argument

##### driver[¶](#jmp-driver "Link to this heading")

Jumpstarter driver CLI tool

```
jmp driver [OPTIONS] COMMAND [ARGS]...
```

Options

--log-level &lt;log\_level&gt;[¶](#cmdoption-jmp-driver-log-level "Link to this definition")

Set the log level

Options:

DEBUG | INFO | WARNING | ERROR | CRITICAL

###### list[¶](#jmp-driver-list "Link to this heading")

```
jmp driver list [OPTIONS]
```

###### version[¶](#jmp-driver-version "Link to this heading")

Get the current Jumpstarter version

```
jmp driver version [OPTIONS]
```

Options

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-driver-version-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

##### get[¶](#jmp-get "Link to this heading")

Display one or many resources

```
jmp get [OPTIONS] COMMAND [ARGS]...
```

###### exporters[¶](#jmp-get-exporters "Link to this heading")

Display one or many exporters

```
jmp get exporters [OPTIONS]
```

Options

--client-config &lt;client\_config&gt;[¶](#cmdoption-jmp-get-exporters-client-config "Link to this definition")

Path to client config

--client &lt;client&gt;[¶](#cmdoption-jmp-get-exporters-client "Link to this definition")

Alias of client config

-l, --selector &lt;selector&gt;[¶](#cmdoption-jmp-get-exporters-l "Link to this definition")

Selector (label query) to filter on, supports ‘=’, ‘==’, and ‘!=’ (e.g. -l key1=value1,key2=value2). Matching objects must satisfy all of the specified label constraints.

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-get-exporters-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

###### leases[¶](#jmp-get-leases "Link to this heading")

Display one or many leases

```
jmp get leases [OPTIONS]
```

Options

--client-config &lt;client\_config&gt;[¶](#cmdoption-jmp-get-leases-client-config "Link to this definition")

Path to client config

--client &lt;client&gt;[¶](#cmdoption-jmp-get-leases-client "Link to this definition")

Alias of client config

-l, --selector &lt;selector&gt;[¶](#cmdoption-jmp-get-leases-l "Link to this definition")

Selector (label query) to filter on, supports ‘=’, ‘==’, and ‘!=’ (e.g. -l key1=value1,key2=value2). Matching objects must satisfy all of the specified label constraints.

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-get-leases-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

##### login[¶](#jmp-login "Link to this heading")

Login into a jumpstarter instance

```
jmp login [OPTIONS]
```

Options

-e, --endpoint &lt;endpoint&gt;[¶](#cmdoption-jmp-login-e "Link to this definition")

Enter the Jumpstarter service endpoint.

--namespace &lt;namespace&gt;[¶](#cmdoption-jmp-login-namespace "Link to this definition")

Enter the Jumpstarter exporter namespace.

--name &lt;name&gt;[¶](#cmdoption-jmp-login-name "Link to this definition")

Enter the Jumpstarter exporter name.

--issuer &lt;issuer&gt;[¶](#cmdoption-jmp-login-issuer "Link to this definition")

OIDC issuer

--client-id &lt;client\_id&gt;[¶](#cmdoption-jmp-login-client-id "Link to this definition")

OIDC client id

--token &lt;token&gt;[¶](#cmdoption-jmp-login-token "Link to this definition")

OIDC access token

--username &lt;username&gt;[¶](#cmdoption-jmp-login-username "Link to this definition")

OIDC username

--password &lt;password&gt;[¶](#cmdoption-jmp-login-password "Link to this definition")

OIDC password

--connector-id &lt;connector\_id&gt;[¶](#cmdoption-jmp-login-connector-id "Link to this definition")

OIDC token exchange connector id (Dex specific)

--allow &lt;allow&gt;[¶](#cmdoption-jmp-login-allow "Link to this definition")

A comma-separated list of driver client packages to load.

--unsafe[¶](#cmdoption-jmp-login-unsafe "Link to this definition")

Should all driver client packages be allowed to load (UNSAFE!).

--insecure-tls-config[¶](#cmdoption-jmp-login-insecure-tls-config "Link to this definition")

Disable endpoint TLS verification. This is insecure and should only be used for testing purposes

--nointeractive[¶](#cmdoption-jmp-login-nointeractive "Link to this definition")

Disable interactive prompts (for use in scripts).

--exporter-config &lt;exporter\_config&gt;[¶](#cmdoption-jmp-login-exporter-config "Link to this definition")

Path of exporter config

--exporter &lt;exporter&gt;[¶](#cmdoption-jmp-login-exporter "Link to this definition")

Alias of exporter config

--client-config &lt;client\_config&gt;[¶](#cmdoption-jmp-login-client-config "Link to this definition")

Path to client config

--client &lt;client&gt;[¶](#cmdoption-jmp-login-client "Link to this definition")

Alias of client config

##### run[¶](#jmp-run "Link to this heading")

Run an exporter locally.

```
jmp run [OPTIONS]
```

Options

--exporter-config &lt;exporter\_config&gt;[¶](#cmdoption-jmp-run-exporter-config "Link to this definition")

Path of exporter config

--exporter &lt;exporter&gt;[¶](#cmdoption-jmp-run-exporter "Link to this definition")

Alias of exporter config

##### shell[¶](#jmp-shell "Link to this heading")

Spawns a shell (or custom command) connecting to a local or remote exporter

COMMAND is the custom command to run instead of shell.

Example:

```
$ jmp shell --exporter foo -- python bar.py
```

```
jmp shell [OPTIONS] [COMMAND]...
```

Options

--exporter-config &lt;exporter\_config&gt;[¶](#cmdoption-jmp-shell-exporter-config "Link to this definition")

Path of exporter config

--exporter &lt;exporter&gt;[¶](#cmdoption-jmp-shell-exporter "Link to this definition")

Alias of exporter config

--client-config &lt;client\_config&gt;[¶](#cmdoption-jmp-shell-client-config "Link to this definition")

Path to client config

--client &lt;client&gt;[¶](#cmdoption-jmp-shell-client "Link to this definition")

Alias of client config

--lease &lt;lease\_name&gt;[¶](#cmdoption-jmp-shell-lease "Link to this definition")

-l, --selector &lt;selector&gt;[¶](#cmdoption-jmp-shell-l "Link to this definition")

Selector (label query) to filter on, supports ‘=’, ‘==’, and ‘!=’ (e.g. -l key1=value1,key2=value2). Matching objects must satisfy all of the specified label constraints.

--duration &lt;duration&gt;[¶](#cmdoption-jmp-shell-duration "Link to this definition")

Accepted duration formats:

PnYnMnDTnHnMnS - ISO 8601 duration format

HH:MM:SS - time in hours, minutes, seconds

D days, HH:MM:SS - time prefixed by X days

D d, HH:MM:SS - time prefixed by X d

See [https://docs.rs/speedate/latest/speedate/](https://docs.rs/speedate/latest/speedate/) for details

Default:

`'00:30:00'`

Arguments

COMMAND[¶](#cmdoption-jmp-shell-arg-COMMAND "Link to this definition")

Optional argument(s)

##### update[¶](#jmp-update "Link to this heading")

Update a resource

```
jmp update [OPTIONS] COMMAND [ARGS]...
```

###### lease[¶](#jmp-update-lease "Link to this heading")

Update a lease

```
jmp update lease [OPTIONS] NAME
```

Options

--client-config &lt;client\_config&gt;[¶](#cmdoption-jmp-update-lease-client-config "Link to this definition")

Path to client config

--client &lt;client&gt;[¶](#cmdoption-jmp-update-lease-client "Link to this definition")

Alias of client config

--duration &lt;duration&gt;[¶](#cmdoption-jmp-update-lease-duration "Link to this definition")

**Required** Accepted duration formats:

PnYnMnDTnHnMnS - ISO 8601 duration format

HH:MM:SS - time in hours, minutes, seconds

D days, HH:MM:SS - time prefixed by X days

D d, HH:MM:SS - time prefixed by X d

See [https://docs.rs/speedate/latest/speedate/](https://docs.rs/speedate/latest/speedate/) for details

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-update-lease-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

Arguments

NAME[¶](#cmdoption-jmp-update-lease-arg-NAME "Link to this definition")

Required argument

##### version[¶](#jmp-version "Link to this heading")

Get the current Jumpstarter version

```
jmp version [OPTIONS]
```

Options

-o, --output &lt;output&gt;[¶](#cmdoption-jmp-version-o "Link to this definition")

Output mode. Use “-o name” for shorter output (resource/name).

Options:

json | yaml | name

#### j[¶](#j "Link to this heading")

The `j` command is available within the Jumpstarter shell environment (launched via `jmp shell`). It provides access to driver CLI interfaces configured in your exporter.

Usage:

```
$ j [OPTIONS] COMMAND [ARGS]...
```

The available commands depend on which drivers are loaded in your current session. When you run the `j` command in the shell:

- Use `j` alone to see all available driver interfaces
- Access specific drivers with `j <driver_type> <action>`
- Each driver exposes different commands through this interface

Available commands vary depending on your configured drivers.

### Package APIs[¶](#package-apis "Link to this heading")

This section provides reference documentation for Jumpstarter’s package APIs and components. The documentation covers:

- [Drivers](#document-reference/package-apis/drivers/index): APIs for various driver categories
- [Exceptions](#document-reference/package-apis/exceptions): Exceptions raised by driver clients

These references are useful for developers extending Jumpstarter or integrating with custom hardware.

#### Driver Packages[¶](#driver-packages "Link to this heading")

This section documents the drivers from the Jumpstarter packages directory. Each driver is contained in a separate package in the form of `jumpstarter-driver-{name}` and provides specific functionality for interacting with different hardware components and systems.

##### Types of Drivers[¶](#types-of-drivers "Link to this heading")

Jumpstarter includes several types of drivers organized by their primary function:

###### System Control Drivers[¶](#system-control-drivers "Link to this heading")

Drivers that control the power state and basic operation of devices:

- [**Power**](#document-reference/package-apis/drivers/power) (`jumpstarter-driver-power`) - Power control for devices
- [**Raspberry Pi**](#document-reference/package-apis/drivers/raspberrypi) (`jumpstarter-driver-raspberrypi`) - Raspberry Pi hardware control
- [**Yepkit**](#document-reference/package-apis/drivers/yepkit) (`jumpstarter-driver-yepkit`) - Yepkit hardware control
- [**DUT Link**](#document-reference/package-apis/drivers/dutlink) (`jumpstarter-driver-dutlink`) - [DUT Link Board](https://github.com/jumpstarter-dev/dutlink-board) hardware control
- [**Energenie PDU**](#document-reference/package-apis/drivers/energenie) (`jumpstarter-driver-energenie`) - Energenie PDUs
- [**Tasmota**](#document-reference/package-apis/drivers/tasmota) (`jumpstarter-driver-tasmota`) - Tasmota hardware control

###### Communication Drivers[¶](#communication-drivers "Link to this heading")

Drivers that provide various communication interfaces:

- [**CAN**](#document-reference/package-apis/drivers/can) (`jumpstarter-driver-can`) - Controller Area Network communication
- [**HTTP**](#document-reference/package-apis/drivers/http) (`jumpstarter-driver-http`) - HTTP communication
- [**Network**](#document-reference/package-apis/drivers/network) (`jumpstarter-driver-network`) - Network interfaces and configuration
- [**PySerial**](#document-reference/package-apis/drivers/pyserial) (`jumpstarter-driver-pyserial`) - Serial port communication
- [**SNMP**](#document-reference/package-apis/drivers/snmp) (`jumpstarter-driver-snmp`) - Simple Network Management Protocol
- [**TFTP**](#document-reference/package-apis/drivers/tftp) (`jumpstarter-driver-tftp`) - Trivial File Transfer Protocol

###### Storage and Data Drivers[¶](#storage-and-data-drivers "Link to this heading")

Drivers that control storage devices and manage data:

- [**OpenDAL**](#document-reference/package-apis/drivers/opendal) (`jumpstarter-driver-opendal`) - Open Data Access Layer
- [**SD Wire**](#document-reference/package-apis/drivers/sdwire) (`jumpstarter-driver-sdwire`) - SD card switching utilities

###### Media Drivers[¶](#media-drivers "Link to this heading")

Drivers that handle media streams:

- [**UStreamer**](#document-reference/package-apis/drivers/ustreamer) (`jumpstarter-driver-ustreamer`) - Video streaming functionality

###### Debug and Programming Drivers[¶](#debug-and-programming-drivers "Link to this heading")

Drivers for debugging and programming devices:

- [**Flashers**](#document-reference/package-apis/drivers/flashers) (`jumpstarter-driver-flashers`) - Flash memory programming tools
- [**Probe-RS**](#document-reference/package-apis/drivers/probe-rs) (`jumpstarter-driver-probe-rs`) - Debugging probe support
- [**QEMU**](#document-reference/package-apis/drivers/qemu) (`jumpstarter-driver-qemu`) - QEMU virtualization platform
- [**Corellium**](#document-reference/package-apis/drivers/corellium) (`jumpstarter-driver-corellium`) - Corellium virtualization platform
- [**U-Boot**](#document-reference/package-apis/drivers/uboot) (`jumpstarter-driver-uboot`) - Universal Bootloader interface

###### Utility Drivers[¶](#utility-drivers "Link to this heading")

General-purpose utility drivers:

- [**Shell**](#document-reference/package-apis/drivers/shell) (`jumpstarter-driver-shell`) - Shell command execution

###### CAN driver[¶](#can-driver "Link to this heading")

`jumpstarter-driver-can` provides functionality for interacting with CAN bus connections based on the [python-can](https://python-can.readthedocs.io/en/stable/index.html) library.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-can
```

###### `jumpstarter_driver_can.Can`[¶](#jumpstarter-driver-can-can "Link to this heading")

A generic CAN bus driver.

Available on any platform, supports many different CAN interfaces through the `python-can` library.

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  can:
    type: jumpstarter_driver_can.Can
    config:
      channel: 1
      interface: "virtual"
```

Parameter

Description

Type

Required

Default

interface

Refer to the [python-can](https://python-can.readthedocs.io/en/stable/interfaces.html) list of interfaces

str

yes

channel

channel to be used, refer to the interface documentation

int or str

yes

###### API Reference[¶](#api-reference "Link to this heading")

*class* jumpstarter\_driver\_can.client.CanClient[¶](#jumpstarter_driver_can.client.CanClient "Link to this definition")

A generic CAN client for sending/recieving traffic to/from an exported CAN bus.

*property* channel\_info*: str*[¶](#jumpstarter_driver_can.client.CanClient.channel_info "Link to this definition")

Get the CAN channel info.

flush\_tx\_buffer() → None[¶](#jumpstarter_driver_can.client.CanClient.flush_tx_buffer "Link to this definition")

Flush the transmission buffer.

*property* protocol*: CanProtocol*[¶](#jumpstarter_driver_can.client.CanClient.protocol "Link to this definition")

Get the CAN protocol supported by the bus.

send(*msg: Message*, *timeout: float | None = None*) → None[¶](#jumpstarter_driver_can.client.CanClient.send "Link to this definition")

Send an individual CAN message.

shutdown() → None[¶](#jumpstarter_driver_can.client.CanClient.shutdown "Link to this definition")

Shutdown the bus.

*property* state*: BusState*[¶](#jumpstarter_driver_can.client.CanClient.state "Link to this definition")

The current state of the CAN bus.

###### `jumpstarter_driver_can.IsoTpPython`[¶](#jumpstarter-driver-can-isotppython "Link to this heading")

A Pure python ISO-TP socket driver

Available on any platform (does not require Linux ISO-TP kernel module), moderate performance and reliability, wide support for non-standard hardware interfaces

###### Configuration[¶](#id1 "Link to this heading")

Example configuration:

```
export:
  can:
    type: jumpstarter_driver_can.IsoTpPython
    config:
      channel: 0
      interface: "virtual"
      address:
        rxid: 1
        txid: 2
      params:
        max_frame_size: 2048
        blocking_send: false
        can_fd: true
```

Parameter

Description

Type

Required

Default

interface

Refer to the [python-can](https://python-can.readthedocs.io/en/stable/interfaces.html) list of interfaces

`str`

no

channel

channel to be used, refer to the interface documentation

`int` or `str`

no

address

Refer to the [isotp.Address](https://can-isotp.readthedocs.io/en/latest/isotp/addressing.html#isotp.Address) documentation

`isotp.Address`

yes

params

IsoTp parameters, refer to the [IsoTpParams](#isotpparams) section table

`IsoTpParams`

no

see table

read\_timeout

Read timeout for the bus in seconds

`float`

no

0.05

###### API Reference[¶](#id2 "Link to this heading")

*class* jumpstarter\_driver\_can.client.IsoTpClient[¶](#jumpstarter_driver_can.client.IsoTpClient "Link to this definition")

An ISO-TP CAN client for sending/recieving ISO-TP frames to/from an exported CAN bus.

available() → bool[¶](#jumpstarter_driver_can.client.IsoTpClient.available "Link to this definition")

Returns True if an ISO-TP frame is awaiting in the reception queue, False otherwise.

recv(*block: bool = False*, *timeout: float | None = None*) → bytes | None[¶](#jumpstarter_driver_can.client.IsoTpClient.recv "Link to this definition")

Dequeue an ISO-TP frame from the reception queue if available.

send(*data: bytes*, *target\_address\_type: int | None = None*, *send\_timeout: float | None = None*) → None[¶](#jumpstarter_driver_can.client.IsoTpClient.send "Link to this definition")

Enqueue an ISO-TP frame to send over the CAN network.

set\_address(*address: Address | AsymmetricAddress*) → None[¶](#jumpstarter_driver_can.client.IsoTpClient.set_address "Link to this definition")

Sets the layer address. Can be set after initialization if needed. May cause a timeout if called while a transmission is active.

start() → None[¶](#jumpstarter_driver_can.client.IsoTpClient.start "Link to this definition")

Start listening for messages.

stop() → None[¶](#jumpstarter_driver_can.client.IsoTpClient.stop "Link to this definition")

Stop listening for messages.

stop\_receiving() → None[¶](#jumpstarter_driver_can.client.IsoTpClient.stop_receiving "Link to this definition")

Stop receiving messages.

stop\_sending() → None[¶](#jumpstarter_driver_can.client.IsoTpClient.stop_sending "Link to this definition")

Stop sending messages.

transmitting() → bool[¶](#jumpstarter_driver_can.client.IsoTpClient.transmitting "Link to this definition")

Returns True if an ISO-TP frame is being transmitted, False otherwise.

###### `jumpstarter_driver_can.IsoTpSocket`[¶](#jumpstarter-driver-can-isotpsocket "Link to this heading")

Pure python ISO-TP socket driver

Available on any platform, moderate performance and reliability, wide support for non-standard hardware interfaces

###### Configuration[¶](#id3 "Link to this heading")

Example configuration:

```
export:
  can:
    type: jumpstarter_driver_can.IsoTpSocket
    config:
      channel: "vcan0"
      address:
        rxid: 1
        txid: 2
      params:
        max_frame_size: 2048
        blocking_send: false
        can_fd: true
```

Parameter

Description

Type

Required

Default

channel

CAN bus to be used i.e. `vcan0`, `vcan1`, etc..

`str`

yes

address

Refer to the [isotp.Address](https://can-isotp.readthedocs.io/en/latest/isotp/addressing.html#isotp.Address) documentation

isotp.Address

yes

params

IsoTp parameters, refer to the [IsoTpParams](#isotpparams) section table

`IsoTpParams`

no

see table

###### API Reference[¶](#id4 "Link to this heading")

*class* jumpstarter\_driver\_can.client.IsoTpClient

An ISO-TP CAN client for sending/recieving ISO-TP frames to/from an exported CAN bus.

available() → bool

Returns True if an ISO-TP frame is awaiting in the reception queue, False otherwise.

recv(*block: bool = False*, *timeout: float | None = None*) → bytes | None

Dequeue an ISO-TP frame from the reception queue if available.

send(*data: bytes*, *target\_address\_type: int | None = None*, *send\_timeout: float | None = None*) → None

Enqueue an ISO-TP frame to send over the CAN network.

set\_address(*address: Address | AsymmetricAddress*) → None

Sets the layer address. Can be set after initialization if needed. May cause a timeout if called while a transmission is active.

start() → None

Start listening for messages.

stop() → None

Stop listening for messages.

stop\_receiving() → None

Stop receiving messages.

stop\_sending() → None

Stop sending messages.

transmitting() → bool

Returns True if an ISO-TP frame is being transmitted, False otherwise.

###### IsoTpParams[¶](#isotpparams "Link to this heading")

Parameter

Description

Type

Required

Default

`stmin`

Minimum Separation Time minimum in milliseconds between consecutive frames.

`int`

No

`0`

`blocksize`

Number of consecutive frames that can be sent before waiting for a flow control frame.

`int`

No

`8`

`tx_data_length`

Default length of data in a transmitted CAN frame (CAN 2.0) or initial frame (CAN FD).

`int`

No

`8`

`tx_data_min_length`

Minimum length of data in a transmitted CAN frame; pads with `tx_padding` if shorter.

`int` | `None`

No

`None`

`override_receiver_stmin`

Override the STmin value (in seconds) received from the receiver; `None` means do not override.

`float` | `None`

No

`None`

`rx_flowcontrol_timeout`

Timeout in milliseconds for receiving a flow control frame after sending a first frame or a block.

`int`

No

`1000`

`rx_consecutive_frame_timeout`

Timeout in milliseconds for receiving a consecutive frame in a multi-frame message.

`int`

No

`1000`

`tx_padding`

Byte value used for padding if the data length is less than `tx_data_min_length` or for CAN FD.

`int` | `None`

No

`None`

`wftmax`

Maximum number of Wait Frame Transmissions (WFTMax) allowed before aborting. `0` means WFTs are not used.

`int`

No

`0`

`max_frame_size`

Maximum size of a single ISO-TP frame that can be processed.

`int`

No

`4095`

`can_fd`

If `True`, enables CAN FD (Flexible Data-Rate) specific ISO-TP handling.

`bool`

No

`False`

`bitrate_switch`

If `True` and `can_fd` is `True`, enables bitrate switching for CAN FD frames.

`bool`

No

`False`

`default_target_address_type`

Default target address type: `0` for Physical (1-to-1), `1` for Functional (1-to-n).

`int`

No

`0`

`rate_limit_enable`

If `True`, enables rate limiting for outgoing frames.

`bool`

No

`False`

`rate_limit_max_bitrate`

Maximum bitrate in bits per second for rate limiting if enabled.

`int`

No

`10000000`

`rate_limit_window_size`

Time window in seconds over which the rate limit is calculated.

`float`

No

`0.2`

`listen_mode`

If `True`, the stack operates in listen-only mode (does not send any frames).

`bool`

No

`False`

`blocking_send`

If `True`, send operations will block until the message is fully transmitted or an error occurs.

`bool`

No

`False`

###### Corellium Driver[¶](#corellium-driver "Link to this heading")

`jumpstarter-driver-corellium` provides functionality for interacting with [Corellium](https://corellium.com) virtualization platform.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-corellium
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  corellium:
    type: jumpstarter_driver_corellium.driver.Corellium
    config:
      project_id: "778f00af-5e9b-40e6-8e7f-c4f14b632e9c"
      device_name: "jmp-rd1ae"
      device_flavor: "kronos"
      # Optional parameters
      # device_os: "1.0"
      # device_build: "Critical Application Monitor (Baremetal)"
```

###### ExporterConfig Example[¶](#exporterconfig-example "Link to this heading")

You can run an exporter by running: `jmp exporter shell -c $file`:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: ExporterConfig
# endpoint and token are intentionally left empty
metadata:
  namespace: default
  name: corellium-demo
endpoint: ""
token: ""
export:
  rd1ae:
    type: jumpstarter_driver_corellium.driver.Corellium
    config:
      project_id: "778f00af-5e9b-40e6-8e7f-c4f14b632e9c"
      device_name: "jmp-rd1ae"
      device_flavor: "kronos"
```

```
apiVersion: jumpstarter.dev/v1alpha1
kind: ExporterConfig
# endpoint and token are intentionally left empty
metadata:
  namespace: default
  name: corellium-demo
endpoint: ""
token: ""
export:
  rd1ae:
    type: jumpstarter_driver_corellium.driver.Corellium
    config:
      project_id: "778f00af-5e9b-40e6-8e7f-c4f14b632e9c"
      device_name: "jmp-rd1ae"
      device_flavor: "kronos"
      device_os: "1.0"
      device_build: "Critical Application Monitor (Baremetal)"
```

###### DUT Link driver[¶](#dut-link-driver "Link to this heading")

`jumpstarter-driver-dutlink` provides functionality for interacting with DUT Link devices.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-dutlink
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  dutlink:
    type: jumpstarter_driver_dutlink.driver.Dutlink
    config:
      # Add required config parameters here
```

###### API Reference[¶](#api-reference "Link to this heading")

Add API documentation here.

###### EnerGenie[¶](#energenie "Link to this heading")

Drivers for EnerGenie products.

###### EnerGenie driver[¶](#energenie-driver "Link to this heading")

This driver provides a client for the [EnerGenie Programmable power switch](https://energenie.com/products.aspx?sg=239). The driver was tested on EG-PMS2-LAN device only but should be easy to support other devices.

**driver**: `jumpstarter_driver_energenie.driver.EnerGenie`

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-energenie
```

###### Configuration[¶](#configuration "Link to this heading")

```
export:
  power:
    type: jumpstarter_driver_energenie.driver.EnerGenie
    config:
      host: "192.168.0.1"
      password: "password"
      slot: "1"
```

###### Config parameters[¶](#config-parameters "Link to this heading")

Parameter

Description

Type

Required

Default

host

The ip address of the EnerGenie system

string

yes

None

password

The password of the EnerGenie system

string

no

None

slot

The slot number to be managed, 1, 2, 3, 4

int

yes

1

###### PowerClient API[¶](#powerclient-api "Link to this heading")

The EnerGenie driver provides a `PowerClient` with the following API:

*class* jumpstarter\_driver\_power.client.PowerClient

###### Examples[¶](#examples "Link to this heading")

Powering on and off a device

```
client.power.on()
time.sleep(1)
client.power.off()
```

###### CLI[¶](#cli "Link to this heading")

```
$ sudo uv run jmp exporter shell -c ./packages/jumpstarter-driver-energenie/examples/exporter.yaml

$$ j
Usage: j [OPTIONS] COMMAND [ARGS]...

  Generic composite device

Options:
  --help  Show this message and exit.

Commands:
  power   Generic power

$$ j power on


$$ exit
```

###### Flashers[¶](#flashers "Link to this heading")

The flasher drivers are used to flash images to DUTs via network, typically using TFTP and HTTP. It is designed to interact with the target bootloader and busybox shell to flash the DUT.

All flasher drivers inherit from the `jumpstarter_driver_flashers.driver.BaseFlasher` class, referencing their own bundle of binary artifacts necessary to flash the DUT, like kernel/initram/dtbs. See the [bundle](#oci-bundles) section for more details.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-flashers
```

###### Available drivers and bundles[¶](#available-drivers-and-bundles "Link to this heading")

Driver

Bundle

TIJ784S4Flasher

quay.io/jumpstarter-dev/jumpstarter-flasher-ti-j784s4:latest

###### Driver configuration[¶](#driver-configuration "Link to this heading")

**driver**: `jumpstarter_driver_flashers.driver.${DRIVER}`

```
export:
  storage:
    type: "jumpstarter_driver_flashers.driver.TIJ784S4Flasher"
    children:
      serial:
        ref: "serial"
      power:
        ref: "power"
  serial:
    type: "jumpstarter_driver_pyserial.driver.PySerial"
    config:
      url: "/dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_112214101760A-if00-port0"
      baudrate: 115200
  power:
    type: jumpstarter_driver_yepkit.driver.Ykush
    config:
      serial: "YK112233"
      port: "1"
```

flasher drivers require four children drivers:

Child Driver

Description

Auto-created

serial

To communicate with the DUT via serial and drive the bootloader and busybox shell

No

power

To power on and off the DUT

No

tftp

To serve binaries via TFTP

Yes

http

To serve the images via HTTP

Yes

The power driver is used to control power cycling of the DUT, and the serial interface is used to communicate with the DUT bootloader via serial. TFTP and HTTP servers are used to serve images to the DUT bootloader and busybox shell.

###### Config parameters[¶](#config-parameters "Link to this heading")

Parameter

Description

Type

Required

Default

flasher\_bundle

The OCI bundle to use for the flasher

str

yes

cache\_dir

The directory to cache the images

str

no

/var/lib/jumpstarter/flasher

tftp\_dir

The directory to serve the images via TFTP

str

no

/var/lib/tftpboot

http\_dir

The directory to serve the images via HTTP

str

no

/var/www/html

###### BaseFlasher API[¶](#baseflasher-api "Link to this heading")

The `BaseFlasher` class provides a set of methods to flash the DUT,

*class* jumpstarter\_driver\_flashers.client.BaseFlasherClient[¶](#jumpstarter_driver_flashers.client.BaseFlasherClient "Link to this definition")

Client interface for software driven flashing

This client provides methods to flash and dump images to a device under test (DUT)

bootloader\_shell()[¶](#jumpstarter_driver_flashers.client.BaseFlasherClient.bootloader_shell "Link to this definition")

Start a context manager uboot/bootloader for interactive console

busybox\_shell()[¶](#jumpstarter_driver_flashers.client.BaseFlasherClient.busybox_shell "Link to this definition")

Start a context manager busybox interactive console

flash(*path: str | PathLike*, *\**, *partition: str | None = None*, *operator: Operator | None = None*, *os\_image\_checksum: str | None = None*, *force\_exporter\_http: bool = False*, *force\_flash\_bundle: str | None = None*)[¶](#jumpstarter_driver_flashers.client.BaseFlasherClient.flash "Link to this definition")

Flash image to DUT

use\_dtb(*path: str | PathLike*, *operator: Operator | None = None*)[¶](#jumpstarter_driver_flashers.client.BaseFlasherClient.use_dtb "Link to this definition")

Use DTB file

use\_initram(*path: str | PathLike*, *operator: Operator | None = None*)[¶](#jumpstarter_driver_flashers.client.BaseFlasherClient.use_initram "Link to this definition")

Use initramfs file

use\_kernel(*path: str | PathLike*, *operator: Operator | None = None*)[¶](#jumpstarter_driver_flashers.client.BaseFlasherClient.use_kernel "Link to this definition")

Use kernel file

###### CLI[¶](#cli "Link to this heading")

The flasher driver provides a CLI to perform flashing, access to busybox shell and uboot.

```
$ jmp shell -l board=ti-03
INFO:jumpstarter.client.lease:Created lease request for labels {'board': 'ti-03'} for 0:30:00
jumpstarter ⚡remote ➤ j storage
Usage: j storage [OPTIONS] COMMAND [ARGS]...

  Software-defined flasher interface

Options:
  --help  Show this message and exit.

Commands:
  bootloader-shell  Start a uboot/bootloader interactive console
  busybox-shell     Start a busybox shell
  flash             Flash image to DUT from file
```

###### flash[¶](#flash "Link to this heading")

```
Usage: j storage flash [OPTIONS] FILE

  Flash image to DUT from file

Options:
  --partition TEXT
  --os-image-checksum TEXT       SHA256 checksum of OS image (direct value)
  --os-image-checksum-file FILE  File containing SHA256 checksum of OS image
  --force-exporter-http          Force use of exporter HTTP
  --force-flash-bundle TEXT      Force use of a specific flasher OCI bundle
  --console-debug                Enable console debug mode
  --help                         Show this message and exit.
```

Example:

```
jumpstarter ⚡remote ➤ j storage flash https://autosd.sig.centos.org/AutoSD-9/nightly/TI/auto-osbuild-am69sk-autosd9-qa-regular-aarch64-1716106242.66b4d866.raw.xz
BaseFlasherClient - INFO - Writing image to storage in the background: /AutoSD-9/nightly/TI/auto-osbuild-am69sk-autosd9-qa-regular-aarch64-1716106242.66b4d866.raw.xz
BaseFlasherClient - INFO - Setting up flasher bundle files in exporter
BaseFlasherClient - INFO - Writing image from storage, with metadata: md5=None,size=592736176 etag="23546fb0-63045567a5b80"
SNMPServerClient - INFO - Starting power cycle sequence
SNMPServerClient - INFO - Waiting 2 seconds...
SNMPServerClient - INFO - Power cycle sequence complete
BaseFlasherClient - INFO - Waiting for U-Boot prompt...
BaseFlasherClient - INFO - Running DHCP to obtain network configuration...
BaseFlasherClient - INFO - Running command: dhcp
BaseFlasherClient - INFO - Running command: printenv netmask
BaseFlasherClient - INFO - discovered dhcp details: DhcpInfo(ip_address='x.x.x.x', gateway='x.x.x.x', netmask='255.255.255.0')
BaseFlasherClient - INFO - Image written to storage: /AutoSD-9/nightly/TI/auto-osbuild-am69sk-autosd9-qa-regular-aarch64-1716106242.66b4d866.raw.xz
BaseFlasherClient - INFO - Running command: setenv serverip 'x.x.x.x'
BaseFlasherClient - INFO - Running command: tftpboot 0x82000000 J784S4XEVM.flasher.img
BaseFlasherClient - INFO - Running command: tftpboot 0x84000000 k3-j784s4-evm.dtb
BaseFlasherClient - INFO - Running boot command: booti 0x82000000 - 0x84000000
BaseFlasherClient - INFO - Using target block device: /dev/mmcblk1
BaseFlasherClient - INFO - Running preflash command: dd if=/dev/zero of=/dev/mmcblk0 bs=512 count=34
BaseFlasherClient - INFO - Running preflash command: dd if=/dev/zero of=/dev/mmcblk1 bs=512 count=34
BaseFlasherClient - INFO - Waiting until the http image preparation in storage is completed
BaseFlasherClient - INFO - Flash progress: 25.00 MB, Speed: 15.78 MB/s
...
...
BaseFlasherClient - INFO - Flash progress: 5086.12 MB, Speed: 13.77 MB/s
BaseFlasherClient - INFO - Flash progress: 5102.94 MB, Speed: 12.93 MB/s
BaseFlasherClient - INFO - Flushing buffers
BaseFlasherClient - INFO - Flashing completed in 7:26
BaseFlasherClient - INFO - Powering off target
```

###### bootloader-shell[¶](#bootloader-shell "Link to this heading")

```
Usage: j storage bootloader-shell [OPTIONS]

  Start a uboot/bootloader interactive console

Options:
  --console-debug  Enable console debug mode
  --help           Show this message and exit.
```

Example

```
jumpstarter ⚡remote ➤ j storage bootloader-shell
BaseFlasherClient - INFO - Setting up flasher bundle files in exporter
SNMPServerClient - INFO - Starting power cycle sequence
SNMPServerClient - INFO - Waiting 2 seconds...
SNMPServerClient - INFO - Power cycle sequence complete
BaseFlasherClient - INFO - Waiting for U-Boot prompt...
=> version
U-Boot 2024.01-rc3 (Jan 09 2024 - 00:00:00 +0000)

gcc (GCC) 11.4.1 20231218 (Red Hat 11.4.1-3)
GNU ld version 2.35.2-42.el9
```

###### busybox-shell[¶](#busybox-shell "Link to this heading")

```
Usage: j storage busybox-shell [OPTIONS]

  Start a busybox interactive console

Options:
  --console-debug  Enable console debug mode
  --help           Show this message and exit.
```

Example

```
jumpstarter ⚡remote ➤ j storage busybox-shell
BaseFlasherClient - INFO - Setting up flasher bundle files in exporter
SNMPServerClient - INFO - Starting power cycle sequence
SNMPServerClient - INFO - Waiting 2 seconds...
SNMPServerClient - INFO - Power cycle sequence complete
BaseFlasherClient - INFO - Waiting for U-Boot prompt...
BaseFlasherClient - INFO - Running DHCP to obtain network configuration...
BaseFlasherClient - INFO - Running command: dhcp
BaseFlasherClient - INFO - Running command: printenv netmask
BaseFlasherClient - INFO - discovered dhcp details: DhcpInfo(ip_address='10.26.28.138', gateway='10.26.28.254', netmask='255.255.255.0')
BaseFlasherClient - INFO - Running command: setenv serverip '10.26.28.62'
BaseFlasherClient - INFO - Running command: tftpboot 0x82000000 J784S4XEVM.flasher.img
BaseFlasherClient - INFO - Running command: tftpboot 0x84000000 k3-j784s4-evm.dtb
BaseFlasherClient - INFO - Running boot command: booti 0x82000000 - 0x84000000
# uname -a
Linux buildroot 6.1.46-dirty #2 SMP PREEMPT Thu Mar 14 14:37:01 UTC 2024 aarch64 GNU/Linux
#
```

###### Examples[¶](#examples "Link to this heading")

Flash the device with a specific image

```
flasherclient.flash("/path/to/image.raw.xz")
```

Flash the device with a specific image from a remote URL

```
flasherclient.flash("https://autosd.sig.centos.org/AutoSD-9/nightly/TI/auto-osbuild-j784s4evm-autosd9-qa-regular-aarch64-1716106242.66b4d866.raw.xz")
```

Flash into a specific partition

```
flasherclient.flash("/path/to/image.raw.xz", partition="emmc")
```

###### Examples of utility consoles[¶](#examples-of-utility-consoles "Link to this heading")

In addition to the flashing mechanisms, the flasher drivers also provide a way to access the DUT bootloader and busybox shell for convenience and debugging, when using the `busybox_shell` and `bootloader_shell` methods the embedded http and tftp servers will be online and serving the images from the flasher bundle.

Get the busybox shell on the device

```
with flasherclient.busybox_shell() as serial:
    serial.send("ls -la\n")
    serial.expect("#")
    print(serial.before)
```

Get the bootloader shell on the device

```
with flasherclient.bootloader_shell() as serial:
    serial.send("version\n")
    serial.expect("=>")
    print(serial.before)
```

###### oci-bundles[¶](#oci-bundles "Link to this heading")

The flasher drivers require some artifacts and basic information about the target device to operate. To make this easy to distribute and use, we use OCI bundles to package the artifacts and metadata.

The bundle is a container that uses [oras](https://oras.land/) to transport the artifacts and metadata. It is a container that contains the following:

- `manifest.yaml`: The manifest file that describes the bundle
- `data/*`: The artifacts, including kernel, initram, dtbs, etc.

###### The format of the manifest is as follows:[¶](#the-format-of-the-manifest-is-as-follows "Link to this heading")

```
# This is a test manifest for the flasher bundle
# It is used to test the flasher bundle, not intended for any production use
apiVersion: jumpstarter.dev/v1alpha1
kind: FlashBundleManifest
metadata:
  name: test-bundle
spec:
  manufacturer: The Jumpstarter Authors
  link: "https://jumpstarter.dev"
  bootcmd: "booti 0x82000000 - 0x84000000"
  default_target: "usd"
  login:
    type: "busybox"
    login_prompt: "login:"
    username: "root"
    password: "password"
    prompt: "#"
  targets:
    usd: "/sys/class/block#4fb0000"
    emmc: "/sys/class/block#4f80000"
  preflash_commands:
    - "dd if=/dev/zero of=/dev/mmcblk0 bs=512 count=34"
    - "dd if=/dev/zero of=/dev/mmcblk1 bs=512 count=34"
  kernel:
    file: data/kernel
    address: "0x82000000"
  initram:
    file: data/initramfs
    address: "0x83000000"
  dtb:
    default: test-dtb
    address: "0x84000000"
    variants:
      test-dtb: data/dtbs/test-dtb.dtb
      alternate: data/dtbs/alternate.dtb
```

###### Table with the spec fields of the manifest:[¶](#table-with-the-spec-fields-of-the-manifest "Link to this heading")

Field

Description

Default

`manufacturer`

Name of the device manufacturer

`link`

URL to device documentation or manufacturer website

`bootcmd`

Command used to boot the device (e.g. booti, bootz)

`default_target`

Default target device to flash to if none specified

`targets`

Map of target names to device paths

`login.type`

Type of login shell

busybox

`login.login_prompt`

Expected login prompt string

login:

`login.username`

Username to log in with, leave empty if not needed

`login.password`

Password for login, leave empty if not needed

`login.prompt`

Shell prompt after successful login

\#

`preflash_commands`

List of commands to run before flashing, useful to clear boot entries, etc

`kernel.file`

Path to kernel image within bundle

`kernel.address`

Memory address to load kernel to

`initram.file`

Path to initramfs within bundle (if any)

`initram.address`

Memory address to load initramfs to (if any)

`dtb.default`

Default DTB variant to use

`dtb.address`

Memory address to load DTB to

`dtb.variants`

Map of DTB variant names to files

###### Examples[¶](#id1 "Link to this heading")

An example bundle for the TI J784S4XEVM looks like this:

```
apiVersion: jumpstarter.dev/v1alpha1
kind: FlashBundleManifest
metadata:
  name: ti-j784s4
spec:
  manufacturer: Texas Instruments
  link: "https://www.ti.com/tool/PROCESSOR-SDK-J784S4"
  bootcmd: "bootm 0x90000000:kernel 0x90000000:initrd 0x88000000"
  shelltype: "busybox"
  login:
    login_prompt: "login:"
    username: "root"
    prompt: "#"
  default_target: "usd"
  targets:
    usd: "/sys/class/block#4fb0000"
    emmc: "/sys/class/block#4f80000"
# removed for now, even if it's our documented procedure, if
# the board is configured to boot from sd or emmc (and not SPI), and
# the flashing of the final image fails, it will result in an un-bootable
# system -> lab admin going to the site and re-flashing SD, this can
# only be avoided by using something like sdwire
#
#  preflash_commands:
#    - "dd if=/dev/zero of=/dev/mmcblk0 bs=512 count=34"
#    - "dd if=/dev/zero of=/dev/mmcblk1 bs=512 count=34"
  kernel:
    file: data/J784S4XEVM.flasher.img
    address: "0x90000000"

  dtb:
    default: j784s4
    address: "0x88000000"
    variants:
      j784s4:
        bootcmd: "bootm 0x90000000#j784s4"
      am69:
        bootcmd: "bootm 0x90000000#am69"
```

You can find a script to build and push a bundle to a registry here: [oci\_bundles](https://github.com/jumpstarter-dev/jumpstarter/tree/main/packages/jumpstarter-driver-flashers/oci_bundles)

###### HTTP driver[¶](#http-driver "Link to this heading")

`jumpstarter-driver-http` provides functionality for HTTP communication.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-http
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  http:
    type: jumpstarter_driver_http.driver.HttpServer
    config:
      # Add required config parameters here
```

###### API Reference[¶](#api-reference "Link to this heading")

Add API documentation here.

###### Network drivers[¶](#network-drivers "Link to this heading")

`jumpstarter-driver-network` provides functionality for interacting with network servers and connections.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-network
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  network:
    type: jumpstarter_driver_network.driver.TcpNetwork
    config:
      # Add required parameters here
```

###### API Reference[¶](#api-reference "Link to this heading")

Network driver classes:

*class* jumpstarter\_driver\_network.driver.TcpNetwork[¶](#jumpstarter_driver_network.driver.TcpNetwork "Link to this definition")

TcpNetwork is a driver for connecting to TCP sockets

```
>>> addr = getfixture("tcp_echo_server") # start a tcp echo server
>>> config = f"""
... type: jumpstarter_driver_network.driver.TcpNetwork
... config:
...   host: {addr[0]} # 127.0.0.1
...   port: {addr[1]} # random port
... """
>>> with run(config) as tcp:
...     with tcp.stream() as conn:
...         conn.send(b"hello")
...         assert conn.receive() == b"hello"
```

*class* jumpstarter\_driver\_network.driver.UdpNetwork[¶](#jumpstarter_driver_network.driver.UdpNetwork "Link to this definition")

UdpNetwork is a driver for connecting to UDP sockets

```
>>> config = f"""
... type: jumpstarter_driver_network.driver.UdpNetwork
... config:
...   host: 127.0.0.1
...   port: 41336
... """
>>> with run(config) as udp:
...     pass
```

*class* jumpstarter\_driver\_network.driver.UnixNetwork[¶](#jumpstarter_driver_network.driver.UnixNetwork "Link to this definition")

UnixNetwork is a driver for connecting to Unix domain sockets

```
>>> config = f"""
... type: jumpstarter_driver_network.driver.UnixNetwork
... config:
...   path: /tmp/example.sock
... """
>>> with run(config) as unix:
...     pass
```

*class* jumpstarter\_driver\_network.driver.EchoNetwork[¶](#jumpstarter_driver_network.driver.EchoNetwork "Link to this definition")

EchoNetwork is a mock driver implementing the NetworkInterface

```
>>> config = """
... type: jumpstarter_driver_network.driver.EchoNetwork
... """
>>> with run(config) as echo:
...     with echo.stream() as conn:
...         conn.send(b"hello")
...         assert conn.receive() == b"hello"
```

Client API:

*class* jumpstarter\_driver\_network.client.NetworkClient[¶](#jumpstarter_driver_network.client.NetworkClient "Link to this definition")

###### OpenDAL driver[¶](#opendal-driver "Link to this heading")

`jumpstarter-driver-opendal` provides functionality for interacting with storages attached to the exporter.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-opendal
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
type: "jumpstarter_driver_opendal.driver.Opendal"
config:
  # See https://docs.rs/opendal/latest/opendal/services/index.html
  # for list of supported services and their configuration parameters
  scheme: "fs"
  kwargs:
    root: "/tmp/jumpstarter"
```

###### API Reference[¶](#api-reference "Link to this heading")

###### Examples[¶](#examples "Link to this heading")

```
>>> from tempfile import NamedTemporaryFile
>>> opendal.create_dir("test/directory/")
>>> opendal.write_bytes("test/directory/file", b"hello")
>>> assert opendal.hash("test/directory/file", "md5") == "5d41402abc4b2a76b9719d911017c592"
>>> opendal.remove_all("test/")
```

###### Client API[¶](#client-api "Link to this heading")

*class* jumpstarter\_driver\_opendal.client.OpendalClient[¶](#jumpstarter_driver_opendal.client.OpendalClient "Link to this definition")

capability() → [Capability](index.html#jumpstarter_driver_opendal.common.Capability "jumpstarter_driver_opendal.common.Capability")[¶](#jumpstarter_driver_opendal.client.OpendalClient.capability "Link to this definition")

Get capabilities of the underlying storage

```
>>> cap = opendal.capability()
>>> cap.copy
True
>>> cap.presign_read
False
```

copy(*source: str | PathLike*, *target: str | PathLike*)[¶](#jumpstarter_driver_opendal.client.OpendalClient.copy "Link to this definition")

Copy source to target

```
>>> opendal.write_bytes("file.txt", b"content")
>>> opendal.copy("file.txt", "copy.txt")
>>> opendal.exists("copy.txt")
True
```

create\_dir(*path: str | PathLike*)[¶](#jumpstarter_driver_opendal.client.OpendalClient.create_dir "Link to this definition")

Create a dir at given path

To indicate that a path is a directory, it is compulsory to include a trailing / in the path.

Create on existing dir will succeed. Create dir is always recursive, works like mkdir -p.

```
>>> opendal.create_dir("a/b/c/")
>>> opendal.exists("a/b/c/")
True
```

delete(*path: str | PathLike*)[¶](#jumpstarter_driver_opendal.client.OpendalClient.delete "Link to this definition")

Delete given path

Delete not existing error won’t return errors

```
>>> opendal.write_bytes("file.txt", b"content")
>>> opendal.exists("file.txt")
True
>>> opendal.delete("file.txt")
>>> opendal.exists("file.txt")
False
```

exists(*path: str | PathLike*) → bool[¶](#jumpstarter_driver_opendal.client.OpendalClient.exists "Link to this definition")

Check if given path exists

```
>>> opendal.exists("file.txt")
False
>>> opendal.write_bytes("file.txt", b"content")
>>> opendal.exists("file.txt")
True
```

hash(*path: str | PathLike*, *algo: Literal\['md5', 'sha256'] = 'sha256'*) → str[¶](#jumpstarter_driver_opendal.client.OpendalClient.hash "Link to this definition")

Get current path’s hash

```
>>> opendal.write_bytes("file.txt", b"content")
>>> opendal.hash("file.txt")
'ed7002b439e9ac845f22357d822bac1444730fbdb6016d3ec9432297b9ec9f73'
```

list(*path: str | PathLike*) → Generator\[str, None, None][¶](#jumpstarter_driver_opendal.client.OpendalClient.list "Link to this definition")

List files and directories under given path

```
>>> opendal.write_bytes("dir/file.txt", b"content")
>>> opendal.write_bytes("dir/another.txt", b"content")
>>> sorted(opendal.list("dir/"))
['dir/', 'dir/another.txt', 'dir/file.txt']
```

open(*path: str | PathLike*, *mode: Literal\['rb', 'wb']*) → [OpendalFile](index.html#jumpstarter_driver_opendal.client.OpendalFile "jumpstarter_driver_opendal.client.OpendalFile")[¶](#jumpstarter_driver_opendal.client.OpendalClient.open "Link to this definition")

Open a file-like reader for the given path

```
>>> file = opendal.open("file.txt", "wb")
>>> file.write_bytes(b"content")
>>> file.close()
```

presign\_read(*path: str | PathLike*, *expire\_second: int*) → [PresignedRequest](index.html#jumpstarter_driver_opendal.common.PresignedRequest "jumpstarter_driver_opendal.common.PresignedRequest")[¶](#jumpstarter_driver_opendal.client.OpendalClient.presign_read "Link to this definition")

Presign an operation for read (GET) which expires after expire\_second seconds

presign\_stat(*path: str | PathLike*, *expire\_second: int*) → [PresignedRequest](index.html#jumpstarter_driver_opendal.common.PresignedRequest "jumpstarter_driver_opendal.common.PresignedRequest")[¶](#jumpstarter_driver_opendal.client.OpendalClient.presign_stat "Link to this definition")

Presign an operation for stat (HEAD) which expires after expire\_second seconds

presign\_write(*path: str | PathLike*, *expire\_second: int*) → [PresignedRequest](index.html#jumpstarter_driver_opendal.common.PresignedRequest "jumpstarter_driver_opendal.common.PresignedRequest")[¶](#jumpstarter_driver_opendal.client.OpendalClient.presign_write "Link to this definition")

Presign an operation for write (PUT) which expires after expire\_second seconds

read\_bytes(*path: str | PathLike*) → bytes[¶](#jumpstarter_driver_opendal.client.OpendalClient.read_bytes "Link to this definition")

Read data from path

```
>>> opendal.write_bytes("file.txt", b"content")
>>> opendal.read_bytes("file.txt")
b'content'
```

read\_into\_path(*src: str | PathLike*, *dst: str | PathLike*, *operator: Operator | None = None*) → None[¶](#jumpstarter_driver_opendal.client.OpendalClient.read_into_path "Link to this definition")

Read data into dst from src

```
>>> opendal.write_bytes("file.txt", b"content")
>>> opendal.read_into_path("file.txt", tmp / "dst")
>>> (tmp / "dst").read_bytes()
b'content'
```

remove\_all(*path: str | PathLike*)[¶](#jumpstarter_driver_opendal.client.OpendalClient.remove_all "Link to this definition")

Remove all file under path

```
>>> opendal.write_bytes("dir/file.txt", b"content")
>>> opendal.remove_all("dir/")
>>> opendal.exists("dir/file.txt")
False
```

rename(*source: str | PathLike*, *target: str | PathLike*)[¶](#jumpstarter_driver_opendal.client.OpendalClient.rename "Link to this definition")

Rename source to target

```
>>> opendal.write_bytes("file.txt", b"content")
>>> opendal.rename("file.txt", "rename.txt")
>>> opendal.exists("file.txt")
False
>>> opendal.exists("rename.txt")
True
```

scan(*path: str | PathLike*) → Generator\[str, None, None][¶](#jumpstarter_driver_opendal.client.OpendalClient.scan "Link to this definition")

List files and directories under given path recursively

```
>>> opendal.write_bytes("dir/a/file.txt", b"content")
>>> opendal.write_bytes("dir/b/another.txt", b"content")
>>> sorted(opendal.scan("dir/"))
['dir/', 'dir/a/', 'dir/a/file.txt', 'dir/b/', 'dir/b/another.txt']
```

stat(*path: str | PathLike*) → [Metadata](index.html#jumpstarter_driver_opendal.common.Metadata "jumpstarter_driver_opendal.common.Metadata")[¶](#jumpstarter_driver_opendal.client.OpendalClient.stat "Link to this definition")

Get current path’s metadata

```
>>> opendal.write_bytes("file.txt", b"content")
>>> opendal.stat("file.txt").mode.is_file()
True
```

write\_bytes(*path: str | PathLike*, *data: bytes*) → None[¶](#jumpstarter_driver_opendal.client.OpendalClient.write_bytes "Link to this definition")

Write data into path

```
>>> opendal.write_bytes("file.txt", b"content")
```

write\_from\_path(*dst: str | PathLike*, *src: str | PathLike*, *operator: Operator | None = None*) → None[¶](#jumpstarter_driver_opendal.client.OpendalClient.write_from_path "Link to this definition")

Write data from src into dst

```
>>> _ = (tmp / "src").write_bytes(b"content")
>>> opendal.write_from_path("file.txt", tmp / "src")
>>> opendal.read_bytes("file.txt")
b'content'
```

*class* jumpstarter\_driver\_opendal.client.OpendalFile[¶](#jumpstarter_driver_opendal.client.OpendalFile "Link to this definition")

A file-like object representing a remote file

close() → None[¶](#jumpstarter_driver_opendal.client.OpendalFile.close "Link to this definition")

Close the file

*property* closed*: bool*[¶](#jumpstarter_driver_opendal.client.OpendalFile.closed "Link to this definition")

Check if the file is closed

read\_into\_path(*path: str | PathLike*, *operator: Operator | None = None*)[¶](#jumpstarter_driver_opendal.client.OpendalFile.read_into_path "Link to this definition")

Read content from remote file into local file

readable() → bool[¶](#jumpstarter_driver_opendal.client.OpendalFile.readable "Link to this definition")

Check if the file is readable

seek(*pos: int*, *whence: int = 0*) → int[¶](#jumpstarter_driver_opendal.client.OpendalFile.seek "Link to this definition")

Change the cursor position to the given byte offset. Offset is interpreted relative to the position indicated by whence. The default value for whence is SEEK\_SET. Values for whence are:

> SEEK\_SET or 0 – start of the file (the default); offset should be zero or positive
> 
> SEEK\_CUR or 1 – current cursor position; offset may be negative
> 
> SEEK\_END or 2 – end of the file; offset is usually negative

Return the new cursor position

seekable() → bool[¶](#jumpstarter_driver_opendal.client.OpendalFile.seekable "Link to this definition")

Check if the file is seekable

tell() → int[¶](#jumpstarter_driver_opendal.client.OpendalFile.tell "Link to this definition")

Return the current cursor position

writable() → bool[¶](#jumpstarter_driver_opendal.client.OpendalFile.writable "Link to this definition")

Check if the file is writable

write\_from\_path(*path: str | PathLike*, *operator: Operator | None = None*)[¶](#jumpstarter_driver_opendal.client.OpendalFile.write_from_path "Link to this definition")

Write into remote file with content from local file

*class* jumpstarter\_driver\_opendal.common.Metadata[¶](#jumpstarter_driver_opendal.common.Metadata "Link to this definition")

content\_disposition*: str | None*[¶](#jumpstarter_driver_opendal.common.Metadata.content_disposition "Link to this definition")

content\_length*: int*[¶](#jumpstarter_driver_opendal.common.Metadata.content_length "Link to this definition")

content\_md5*: str | None*[¶](#jumpstarter_driver_opendal.common.Metadata.content_md5 "Link to this definition")

content\_type*: str | None*[¶](#jumpstarter_driver_opendal.common.Metadata.content_type "Link to this definition")

etag*: str | None*[¶](#jumpstarter_driver_opendal.common.Metadata.etag "Link to this definition")

mode*: [EntryMode](index.html#jumpstarter_driver_opendal.common.EntryMode "jumpstarter_driver_opendal.common.EntryMode")*[¶](#jumpstarter_driver_opendal.common.Metadata.mode "Link to this definition")

*class* jumpstarter\_driver\_opendal.common.EntryMode[¶](#jumpstarter_driver_opendal.common.EntryMode "Link to this definition")

entry\_is\_dir*: bool*[¶](#jumpstarter_driver_opendal.common.EntryMode.entry_is_dir "Link to this definition")

entry\_is\_file*: bool*[¶](#jumpstarter_driver_opendal.common.EntryMode.entry_is_file "Link to this definition")

is\_dir() → bool[¶](#jumpstarter_driver_opendal.common.EntryMode.is_dir "Link to this definition")

is\_file() → bool[¶](#jumpstarter_driver_opendal.common.EntryMode.is_file "Link to this definition")

*class* jumpstarter\_driver\_opendal.common.PresignedRequest[¶](#jumpstarter_driver_opendal.common.PresignedRequest "Link to this definition")

Presigned HTTP request

Allows you to delegate access to a specific file in your storage backend without sharing access credentials

headers*: dict\[str, str]*[¶](#jumpstarter_driver_opendal.common.PresignedRequest.headers "Link to this definition")

Additional HTTP headers to send with the request

method*: str*[¶](#jumpstarter_driver_opendal.common.PresignedRequest.method "Link to this definition")

HTTP method

> GET: download file
> 
> PUT: upload file
> 
> DELETE: delete file

url*: str*[¶](#jumpstarter_driver_opendal.common.PresignedRequest.url "Link to this definition")

HTTP request URL

*class* jumpstarter\_driver\_opendal.common.Capability[¶](#jumpstarter_driver_opendal.common.Capability "Link to this definition")

blocking*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.blocking "Link to this definition")

create\_dir*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.create_dir "Link to this definition")

delete*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.delete "Link to this definition")

list*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.list "Link to this definition")

list\_with\_limit*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.list_with_limit "Link to this definition")

list\_with\_recursive*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.list_with_recursive "Link to this definition")

list\_with\_start\_after*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.list_with_start_after "Link to this definition")

presign*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.presign "Link to this definition")

presign\_read*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.presign_read "Link to this definition")

presign\_stat*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.presign_stat "Link to this definition")

presign\_write*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.presign_write "Link to this definition")

read*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.read "Link to this definition")

read\_with\_if\_match*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.read_with_if_match "Link to this definition")

read\_with\_if\_none\_match*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.read_with_if_none_match "Link to this definition")

read\_with\_override\_cache\_control*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.read_with_override_cache_control "Link to this definition")

read\_with\_override\_content\_disposition*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.read_with_override_content_disposition "Link to this definition")

read\_with\_override\_content\_type*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.read_with_override_content_type "Link to this definition")

rename*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.rename "Link to this definition")

shared*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.shared "Link to this definition")

stat*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.stat "Link to this definition")

stat\_with\_if\_match*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.stat_with_if_match "Link to this definition")

stat\_with\_if\_none\_match*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.stat_with_if_none_match "Link to this definition")

write*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.write "Link to this definition")

write\_can\_append*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.write_can_append "Link to this definition")

write\_can\_empty*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.write_can_empty "Link to this definition")

write\_can\_multi*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.write_can_multi "Link to this definition")

write\_multi\_max\_size*: int | None*[¶](#jumpstarter_driver_opendal.common.Capability.write_multi_max_size "Link to this definition")

write\_multi\_min\_size*: int | None*[¶](#jumpstarter_driver_opendal.common.Capability.write_multi_min_size "Link to this definition")

write\_total\_max\_size*: int | None*[¶](#jumpstarter_driver_opendal.common.Capability.write_total_max_size "Link to this definition")

write\_with\_cache\_control*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.write_with_cache_control "Link to this definition")

write\_with\_content\_disposition*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.write_with_content_disposition "Link to this definition")

write\_with\_content\_type*: bool*[¶](#jumpstarter_driver_opendal.common.Capability.write_with_content_type "Link to this definition")

###### Power driver[¶](#power-driver "Link to this heading")

`jumpstarter-driver-power` provides functionality for interacting with power control devices.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-power
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  power:
    type: jumpstarter_driver_power.driver.MockPower
    config:
      # Add required config parameters here
```

###### API Reference[¶](#api-reference "Link to this heading")

Add API documentation here.

###### probe-rs driver[¶](#probe-rs-driver "Link to this heading")

`jumpstarter-driver-probe-rs` provides functionality for remote debugging and flashing of embedded devices using the [probe-rs](https://probe.rs) tools.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-probe-rs
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  probe:
    type: jumpstarter_driver_probe_rs.driver.ProbeRs
    config:
      probe: "2e8a:000c:5798DE5E500ACB60"
      probe_rs_path: "/home/majopela/.cargo/bin/probe-rs"
      chip: "RP2350"
      protocol: "swd"
      connect_under_reset: false
```

###### Config parameters[¶](#config-parameters "Link to this heading")

Parameter

Description

Type

Required

Default

probe

The probe id, can be in VID:PID format or VID:PID:SERIALNUMBER

str

no

probe\_rs\_path

The path to the probe-rs binary

str

no

probe-rs

chip

The target chip

str

no

protocol

The target protocol

“swd” or “jtag”

no

connect\_under\_reset

Connect to the target while asserting reset

bool

no

false

###### API Reference[¶](#api-reference "Link to this heading")

*class* jumpstarter\_driver\_probe\_rs.client.ProbeRsClient[¶](#jumpstarter_driver_probe_rs.client.ProbeRsClient "Link to this definition")

Client interface for probe-rs driver.

This client provides methods to use probe-rs remotely.

download(*operator: Operator*, *path: str*) → str[¶](#jumpstarter_driver_probe_rs.client.ProbeRsClient.download "Link to this definition")

Download a file to the device

download\_file(*filepath*) → str[¶](#jumpstarter_driver_probe_rs.client.ProbeRsClient.download_file "Link to this definition")

Download a local file to the device

erase() → str[¶](#jumpstarter_driver_probe_rs.client.ProbeRsClient.erase "Link to this definition")

Erase the target memory, this is generally a slow operation.

info() → str[¶](#jumpstarter_driver_probe_rs.client.ProbeRsClient.info "Link to this definition")

Get probe-rs information about the target

read(*width: int*, *address: int*, *words: int*) → list\[int][¶](#jumpstarter_driver_probe_rs.client.ProbeRsClient.read "Link to this definition")

Read from memory

Args:

- width: the width of the data to read, 8, 16, 32 or 64
- address: the address to read from
- words: the number of words to read

reset() → str[¶](#jumpstarter_driver_probe_rs.client.ProbeRsClient.reset "Link to this definition")

Reset the target, must be used after download to start the target

###### CLI[¶](#cli "Link to this heading")

The probe driver client comes with a CLI tool that can be used to interact with the target device.

```
jumpstarter ⚡ local ➤ j probe
Usage: j probe [OPTIONS] COMMAND [ARGS]...

  probe-rs client

Options:
  --help  Show this message and exit.

Commands:
  download  Download a file to the target
  erase     Erase the target, this is a slow operation.
  info      Get target information
  read      read from target memory
  reset     Reset the target
```

###### PySerial driver[¶](#pyserial-driver "Link to this heading")

`jumpstarter-driver-pyserial` provides functionality for serial port communication.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-pyserial
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  serial:
    type: jumpstarter_driver_pyserial.driver.PySerial
    config:
      url: "/dev/ttyUSB0"
      baudrate: 115200
```

###### Config parameters[¶](#config-parameters "Link to this heading")

Parameter

Description

Type

Required

Default

url

The serial port to connect to, in [pyserial format](https://pyserial.readthedocs.io/en/latest/url_handlers.html)

str

yes

baudrate

The baudrate to use for the serial connection

int

no

115200

check\_existing

Check if the serial port exists during exporter initialization, disable if you are connecting to a dynamically created port (i.e. USB from your DUT)

bool

no

True

###### API Reference[¶](#api-reference "Link to this heading")

*class* jumpstarter\_driver\_pyserial.client.PySerialClient[¶](#jumpstarter_driver_pyserial.client.PySerialClient "Link to this definition")

A client for handling serial communication using pexpect.

close()[¶](#jumpstarter_driver_pyserial.client.PySerialClient.close "Link to this definition")

Close the open stream session without a context manager.

open() → fdspawn[¶](#jumpstarter_driver_pyserial.client.PySerialClient.open "Link to this definition")

Open a pexpect session. You can find the pexpect documentation here: [https://pexpect.readthedocs.io/en/stable/api/pexpect.html#spawn-class](https://pexpect.readthedocs.io/en/stable/api/pexpect.html#spawn-class)

Returns:

fdspawn: The pexpect session object.

open\_stream() → BlockingStream[¶](#jumpstarter_driver_pyserial.client.PySerialClient.open_stream "Link to this definition")

Open a blocking stream session without a context manager.

Returns:

blocking stream session object.

Return type:

BlockingStream

pexpect()[¶](#jumpstarter_driver_pyserial.client.PySerialClient.pexpect "Link to this definition")

Create a pexpect adapter context manager.

Yields:

PexpectAdapter: The pexpect adapter object.

stream(*method='connect'*)[¶](#jumpstarter_driver_pyserial.client.PySerialClient.stream "Link to this definition")

Open a blocking stream session with a context manager.

Parameters:

**method** (*str*) – method name of streaming driver call

Returns:

blocking stream session object context manager.

###### Examples[¶](#examples "Link to this heading")

Using expect with a context manager

```
with pyserialclient.pexpect() as session:
    session.sendline("Hello, world!")
    session.expect("Hello, world!")
```

Using expect without a context manager

```
session = pyserialclient.open()
session.sendline("Hello, world!")
session.expect("Hello, world!")
pyserialclient.close()
```

Using a simple BlockingStream with a context manager

```
with pyserialclient.stream() as stream:
    stream.send(b"Hello, world!")
    data = stream.receive()
```

Using a simple BlockingStream without a context manager

```
stream = pyserialclient.open_stream()
stream.send(b"Hello, world!")
data = stream.receive()
```

###### QEMU driver[¶](#qemu-driver "Link to this heading")

`jumpstarter-driver-qemu` provides functionality for interacting with QEMU virtualization platform.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-qemu
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  qemu:
    type: jumpstarter_driver_qemu.driver.Qemu
    config:
      # Add required config parameters here
```

###### API Reference[¶](#api-reference "Link to this heading")

Add API documentation here.

###### Raspberry Pi driver[¶](#raspberry-pi-driver "Link to this heading")

`jumpstarter-driver-raspberrypi` provides functionality for interacting with Raspberry Pi devices.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-raspberrypi
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  raspberrypi:
    type: jumpstarter_driver_raspberrypi.driver.DigitalOutput
    config:
      # Add required config parameters here
```

###### API Reference[¶](#api-reference "Link to this heading")

Add API documentation here.

###### SDWire driver[¶](#sdwire-driver "Link to this heading")

`jumpstarter-driver-sdwire` provides functionality for using the SDWire storage multiplexer. This device multiplexes an SD card between the DUT and the exporter host.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-sdwire
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
type: "jumpstarter_driver_sdwire.driver.SDWire"
config:
  # optional serial number of the sd-wire device
  # the first one found would be used if unset
  serial: "sdw-00001"
  # optional path to the block device exposed by sd-wire
  # automatically detected if unset
  storage_device: "/dev/disk/by-diskseq/1"
```

###### API Reference[¶](#api-reference "Link to this heading")

The SDWire driver implements the `StorageMuxClient` class, which is a generic storage class.

*class* jumpstarter\_driver\_opendal.client.StorageMuxClient[¶](#jumpstarter_driver_opendal.client.StorageMuxClient "Link to this definition")

dut()[¶](#jumpstarter_driver_opendal.client.StorageMuxClient.dut "Link to this definition")

Connect storage to dut

host()[¶](#jumpstarter_driver_opendal.client.StorageMuxClient.host "Link to this definition")

Connect storage to host

off()[¶](#jumpstarter_driver_opendal.client.StorageMuxClient.off "Link to this definition")

Disconnect storage

read\_local\_file(*filepath*)[¶](#jumpstarter_driver_opendal.client.StorageMuxClient.read_local_file "Link to this definition")

Read into a local file from the storage device

write\_local\_file(*filepath*)[¶](#jumpstarter_driver_opendal.client.StorageMuxClient.write_local_file "Link to this definition")

Write a local file to the storage device

###### Shell driver[¶](#shell-driver "Link to this heading")

`jumpstarter-driver-shell` provides functionality for shell command execution.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-shell
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  shell:
    type: jumpstarter_driver_shell.driver.Shell
    config:
      methods:
        ls: "ls"
        method2: "echo 'Hello World 2'"
        #multi line method
        method3: |
          echo 'Hello World $1'
          echo 'Hello World $2'
        env_var: "echo $1,$2,$ENV_VAR"
      # optional parameters
      cwd: "/tmp"
      log_level: "INFO"
      shell:
        - "/bin/bash"
        - "-c"
```

###### API Reference[¶](#api-reference "Link to this heading")

Assuming the exporter driver is configured as in the example above, the client methods will be generated dynamically, and they will be available as follows:

*class* jumpstarter\_driver\_shell.client.ShellClient(*\**, *uuid: uuid.UUID = &lt;factory&gt;*, *labels: dict\[str*, *str] = &lt;factory&gt;*, *stub: Any*, *log\_level: str = 'INFO'*, *children: 'dict\[str*, *DriverClient]' = &lt;factory&gt;*, *portal: 'BlockingPortal'*, *stack: 'ExitStack'*)[¶](#jumpstarter_driver_shell.client.ShellClient "Link to this definition")

ls()

Returns:

A tuple(stdout, stderr, return\_code)

method2()

Returns:

A tuple(stdout, stderr, return\_code)

method3(*arg1*, *arg2*)

Returns:

A tuple(stdout, stderr, return\_code)

env\_var(*arg1*, *arg2*, *ENV\_VAR='value'*)

Returns:

A tuple(stdout, stderr, return\_code)

###### SNMP driver[¶](#snmp-driver "Link to this heading")

`jumpstarter-driver-snmp` provides functionality for controlling power via SNMP-enabled PDUs (Power Distribution Units).

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-snmp
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  power:
    type: jumpstarter_driver_snmp.driver.SNMPServer
    config:
      host: "pdu.mgmt.com"
      user: "labuser"
      plug: 32
      port: 161
      oid: "1.3.6.1.4.1.13742.6.4.1.2.1.2.1"
      auth_protocol: "NONE"
      auth_key: null
      priv_protocol: "NONE"
      priv_key: null
      timeout: 5.0
```

###### Config parameters[¶](#config-parameters "Link to this heading")

Parameter

Description

Type

Required

Default

host

Hostname or IP address of the SNMP-enabled PDU

str

yes

user

SNMP v3 username

str

yes

plug

PDU outlet number to control

int

yes

port

SNMP port number

int

no

161

oid

Base OID for power control

str

no

“1.3.6.1.4.1.13742.6.4.1.2.1.2.1”

auth\_protocol

Authentication protocol (“NONE”, “MD5”, “SHA”)

str

no

“NONE”

auth\_key

Authentication key when auth\_protocol is not “NONE”

str

no

null

priv\_protocol

Privacy protocol (“NONE”, “DES”, “AES”)

str

no

“NONE”

priv\_key

Privacy key when priv\_protocol is not “NONE”

str

no

null

timeout

SNMP timeout in seconds

float

no

5.0

###### API Reference[¶](#api-reference "Link to this heading")

*class* jumpstarter\_driver\_snmp.client.SNMPServerClient[¶](#jumpstarter_driver_snmp.client.SNMPServerClient "Link to this definition")

Bases: [`PowerClient`](index.html#jumpstarter_driver_power.client.PowerClient "jumpstarter_driver_power.client.PowerClient")

Client interface for SNMP Power Control

off()[¶](#jumpstarter_driver_snmp.client.SNMPServerClient.off "Link to this definition")

Turn power off

on()[¶](#jumpstarter_driver_snmp.client.SNMPServerClient.on "Link to this definition")

Turn power on

###### Examples[¶](#examples "Link to this heading")

Power cycling a device:

```
snmp_client.cycle(wait=3)
```

Basic power control:

```
snmp_client.off()
snmp_client.on()
```

Using the CLI:

```
j power on
j power off
j power cycle --wait 3
```

###### Tasmota driver[¶](#tasmota-driver "Link to this heading")

`jumpstarter-driver-tasmota` provides functionality for interacting with tasmota compatible devices.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-tasmota
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  power:
    type: jumpstarter_driver_tasmota.driver.TasmotaPower
```

###### Config parameters[¶](#config-parameters "Link to this heading")

Parameter

Description

Default

`host`

MQTT broker hostname or IP address

Required

`port`

MQTT broker port

1883

`tls`

MQTT broker TLS enabled

True

`client_id`

Client identifier for MQTT connection

`transport`

Transport protocol, one of “tcp”, “websockets”, “unix”

“tcp”

`timeout`

Timeout in seconds for operations

`username`

Username for MQTT authentication

`password`

Password for MQTT authentication

`cmnd_topic`

MQTT topic for sending commands to the Tasmota device

Required

`stat_topic`

MQTT topic for receiving status updates from the Tasmota device

Required

###### API Reference[¶](#api-reference "Link to this heading")

The tasmota power driver provides a `PowerClient` with the following API:

*class* jumpstarter\_driver\_power.client.PowerClient

###### TFTP driver[¶](#tftp-driver "Link to this heading")

`jumpstarter-driver-tftp` provides functionality for a read-only TFTP server that can be used to serve files.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-tftp
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  tftp:
    type: jumpstarter_driver_tftp.driver.Tftp
    config:
      root_dir: /var/lib/tftpboot  # Directory to serve files from
      host: 192.168.1.100          # Host IP to bind to (optional)
      port: 69                     # Port to listen on (optional)
```

###### Config parameters[¶](#config-parameters "Link to this heading")

Parameter

Description

Type

Required

Default

root\_dir

Root directory for the TFTP server

str

no

“/var/lib/tftpboot”

host

IP address to bind the server to

str

no

auto-detect

port

Port number to listen on

int

no

69

###### API Reference[¶](#api-reference "Link to this heading")

*class* jumpstarter\_driver\_tftp.client.TftpServerClient[¶](#jumpstarter_driver_tftp.client.TftpServerClient "Link to this definition")

Bases: `CompositeClient`

Client interface for TFTP Server driver

This client provides methods to control a TFTP server and manage files on it. Supports file operations like uploading from various storage backends through OpenDAL.

get\_host() → str[¶](#jumpstarter_driver_tftp.client.TftpServerClient.get_host "Link to this definition")

Get the host address the TFTP server is listening on

Returns:

str: The IP address or hostname the server is bound to

get\_port() → int[¶](#jumpstarter_driver_tftp.client.TftpServerClient.get_port "Link to this definition")

Get the port number the TFTP server is listening on

Returns:

int: The port number (default is 69)

start()[¶](#jumpstarter_driver_tftp.client.TftpServerClient.start "Link to this definition")

Start the TFTP server

Initializes and starts the TFTP server if it’s not already running. The server will listen on the configured host and port.

stop()[¶](#jumpstarter_driver_tftp.client.TftpServerClient.stop "Link to this definition")

Stop the TFTP server

Stops the running TFTP server and releases associated resources.

Raises:

ServerNotRunning: If the server is not currently running

###### Exception Classes[¶](#exception-classes "Link to this heading")

*class* jumpstarter\_driver\_tftp.driver.TftpError[¶](#jumpstarter_driver_tftp.driver.TftpError "Link to this definition")

Bases: `Exception`

Base exception for TFTP server errors

*class* jumpstarter\_driver\_tftp.driver.ServerNotRunning[¶](#jumpstarter_driver_tftp.driver.ServerNotRunning "Link to this definition")

Bases: [`TftpError`](#jumpstarter_driver_tftp.driver.TftpError "jumpstarter_driver_tftp.driver.TftpError")

Server is not running

###### Examples[¶](#examples "Link to this heading")

```
>>> import tempfile
>>> import os
>>> from jumpstarter_driver_tftp.driver import Tftp
>>> from jumpstarter.common.utils import serve
>>> with tempfile.TemporaryDirectory() as tmp_dir:
...     # Create a test file
...     test_file = os.path.join(tmp_dir, "test.txt")
...     with open(test_file, "w") as f:
...         _ = f.write("hello")
...
...     # Start TFTP server
...     with serve(Tftp(root_dir=tmp_dir, host="127.0.0.1", port=6969)) as tftp:
...         tftp.start()
...
...         # List files
...         files = list(tftp.storage.list("/"))
...         assert "test.txt" in files
...
...         tftp.stop()
```

###### U-Boot driver[¶](#u-boot-driver "Link to this heading")

`jumpstarter-driver-uboot` provides functionality for interacting with the U-Boot bootloader. This driver does not interact with the DUT directly, instead it should be configured with backing power and serial drivers.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-uboot
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
type: "jumpstarter_driver_uboot.driver.UbootConsole"
children:
  power:
    type: "jumpstarter_driver_power.driver.MockPower"
    config: {} # omitted, power driver configuration
  serial:
    type: "jumpstarter_driver_pyserial.driver.PySerial"
    config: # omitted, serial driver configuration
      url: "loop://"
      # instead of configuring the power and serial driver inline
      # other drivers configured on the exporter can also be referenced
      # power:
      #   ref: "dutlink.power"
      # serial:
      #   ref: "dutlink.console"
config:
  prompt: "=>" # the u-boot command prompt to expect, defaults to "=>"
```

###### API Reference[¶](#api-reference "Link to this heading")

*class* jumpstarter\_driver\_uboot.client.UbootConsoleClient[¶](#jumpstarter_driver_uboot.client.UbootConsoleClient "Link to this definition")

get\_env(*key: str*, *timeout: int = 5*) → str | None[¶](#jumpstarter_driver_uboot.client.UbootConsoleClient.get_env "Link to this definition")

Get U-Boot environment variable value

*property* prompt*: str*[¶](#jumpstarter_driver_uboot.client.UbootConsoleClient.prompt "Link to this definition")

U-Boot prompt to expect

reboot\_to\_console(*\**, *debug=False*) → Generator\[None][¶](#jumpstarter_driver_uboot.client.UbootConsoleClient.reboot_to_console "Link to this definition")

Reboot to U-Boot console

Power cycle the target and wait for the U-Boot prompt

Must be used as a context manager, other methods can only be used within the reboot\_to\_console context

```
>>> with uboot.reboot_to_console(debug=True): 
...     uboot.set_env("foo", "bar")
...     uboot.setup_dhcp()
>>> # uboot.set_env("foo", "baz") # invalid use
```

run\_command(*cmd: str*, *timeout: int = 60*, *\**, *\_internal\_log=True*) → bytes[¶](#jumpstarter_driver_uboot.client.UbootConsoleClient.run_command "Link to this definition")

Run raw command in the U-Boot console

run\_command\_checked(*cmd: str*, *timeout: int = 60*, *check=True*) → list\[str][¶](#jumpstarter_driver_uboot.client.UbootConsoleClient.run_command_checked "Link to this definition")

Run command in the U-Boot console and check the exit code

set\_env(*key: str*, *value: str | None*, *timeout: int = 5*) → None[¶](#jumpstarter_driver_uboot.client.UbootConsoleClient.set_env "Link to this definition")

Set U-Boot environment variable value

set\_env\_dict(*env: dict\[str, str | None]*) → None[¶](#jumpstarter_driver_uboot.client.UbootConsoleClient.set_env_dict "Link to this definition")

Set multiple U-Boot environment variable value

setup\_dhcp(*timeout: int = 60*) → DhcpInfo[¶](#jumpstarter_driver_uboot.client.UbootConsoleClient.setup_dhcp "Link to this definition")

Setup dhcp in U-Boot

###### Ustreamer driver[¶](#ustreamer-driver "Link to this heading")

`jumpstarter-driver-ustreamer` provides functionality for using the ustreamer video streaming server driven by the jumpstarter exporter. This driver takes a video device and exposes both snapshot and streaming interfaces.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-ustreamer
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
type: "jumpstarter_driver_ustreamer.driver.UStreamer"
config:
  # name or path of the ustreamer executable
  # defaults to finding ustreamer from path
  executable: "ustreamer"
  args: # extra arguments to pass to ustreamer
    brightness: auto # --brightness=auto
    contrast: default # --contract=default
```

###### API Reference[¶](#api-reference "Link to this heading")

*class* jumpstarter\_driver\_ustreamer.client.UStreamerClient[¶](#jumpstarter_driver_ustreamer.client.UStreamerClient "Link to this definition")

UStreamer client class

Client methods for the UStreamer driver.

snapshot()[¶](#jumpstarter_driver_ustreamer.client.UStreamerClient.snapshot "Link to this definition")

Get a snapshot image from the video input

Returns:

PIL Image object of the snapshot image

Return type:

PIL.Image

state()[¶](#jumpstarter_driver_ustreamer.client.UStreamerClient.state "Link to this definition")

Get state of ustreamer service

###### Yepkit driver[¶](#yepkit-driver "Link to this heading")

`jumpstarter-driver-yepkit` provides functionality for interacting with Yepkit products.

###### Installation[¶](#installation "Link to this heading")

```
$ pip3 install --extra-index-url https://pkg.jumpstarter.dev/simple jumpstarter-driver-yepkit
```

###### Configuration[¶](#configuration "Link to this heading")

Example configuration:

```
export:
  power:
    type: jumpstarter_driver_yepkit.driver.Ykush
    config:
      serial: "YK25838"
      port: "1"

  power2:
    type: jumpstarter_driver_yepkit.driver.Ykush
    config:
      serial: "YK25838"
      port: "2"
```

###### Config parameters[¶](#config-parameters "Link to this heading")

Parameter

Description

Type

Required

Default

serial

The serial number of the ykush hub, empty means auto-detection

no

None

port

The port number to be managed, “0”, “1”, “2”, “a” which means all

str

yes

“a”

###### API Reference[¶](#api-reference "Link to this heading")

The yepkit ykush driver provides a `PowerClient` with the following API:

*class* jumpstarter\_driver\_power.client.PowerClient[¶](#jumpstarter_driver_power.client.PowerClient "Link to this definition")

###### Examples[¶](#examples "Link to this heading")

Powering on and off a device

```
client.power.on()
time.sleep(1)
client.power.off()
```

###### CLI access[¶](#cli-access "Link to this heading")

```
$ sudo ~/.cargo/bin/uv run jmp shell --exporter-config ./packages/jumpstarter-driver-yepkit/examples/exporter.yaml
WARNING:Ykush:No serial number provided for ykush, using the first one found: YK25838
INFO:Ykush:Power OFF for Ykush YK25838 on port 1
INFO:Ykush:Power OFF for Ykush YK25838 on port 2

$$ j
Usage: j [OPTIONS] COMMAND [ARGS]...

  Generic composite device

Options:
  --help  Show this message and exit.

Commands:
  power   Generic power
  power2  Generic power

$$ j power on
INFO:Ykush:Power ON for Ykush YK25838 on port 1

$$ exit
```

#### Exceptions[¶](#exceptions "Link to this heading")

##### API Reference[¶](#module-jumpstarter.common.exceptions "Link to this heading")

*exception* jumpstarter.common.exceptions.ArgumentError(*message: str*)[¶](#jumpstarter.common.exceptions.ArgumentError "Link to this definition")

Raised when a cli argument is not valid.

*exception* jumpstarter.common.exceptions.ConfigurationError(*message: str*)[¶](#jumpstarter.common.exceptions.ConfigurationError "Link to this definition")

Raised when a configuration error exists.

*exception* jumpstarter.common.exceptions.ConnectionError(*message: str*)[¶](#jumpstarter.common.exceptions.ConnectionError "Link to this definition")

Raised when a connection to a jumpstarter server fails.

*exception* jumpstarter.common.exceptions.FileAccessError(*message: str*)[¶](#jumpstarter.common.exceptions.FileAccessError "Link to this definition")

Raised when a file access error occurs.

*exception* jumpstarter.common.exceptions.FileNotFoundError(*message: str*)[¶](#jumpstarter.common.exceptions.FileNotFoundError "Link to this definition")

Raised when a file is not found.

*exception* jumpstarter.common.exceptions.JumpstarterException(*message: str*)[¶](#jumpstarter.common.exceptions.JumpstarterException "Link to this definition")

Base class for jumpstarter-specific errors.

This class should not be raised directly, but should be used as a base class for all jumpstarter-specific errors. It handles the \_\_cause\__ attribute so the jumpstarter errors could be raised as

```
raise SomeError("message") from original_exception
```

© Copyright 2025, Jumpstarter Contributors.
