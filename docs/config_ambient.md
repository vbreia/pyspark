# Preparing the environment to use PySpark

## Java ☕

To run PySpark, we will need to configure the environment with Java. Below is the tutorial for installing all Java dependencies via APT on Ubuntu

To install this version, first update the package index.
```sudo apt update```

To install this version, first update the package index.
```java -version```

Run the following command to install the default Java Runtime Environment (JRE), which will install the OpenJDK 11 JRE:
JRE will allow you to run almost all Java software.
```sudo apt install default-jre```

Verify the installation with:
```java -version```

Also install the Java Development Kit (JDK) in addition to the JRE to compile and run some specific Java-based software.
To install the JDK, run the following command, which will also install the JRE:
```sudo apt install default-jdk```

Verify the installation with:
```javac -version```