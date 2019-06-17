#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-logging
Version  : 1.0.3
Release  : 1
URL      : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.0.3/commons-logging-1.0.3.jar
Source0  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.0.3/commons-logging-1.0.3.jar
Source1  : https://repo1.maven.org/maven2/commons-logging/commons-logging-api/1.1/commons-logging-api-1.1.jar
Source2  : https://repo1.maven.org/maven2/commons-logging/commons-logging-api/1.1/commons-logging-api-1.1.pom
Source3  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.0.3/commons-logging-1.0.3.pom
Source4  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.0.4/commons-logging-1.0.4.jar
Source5  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.0.4/commons-logging-1.0.4.pom
Source6  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.0/commons-logging-1.0.jar
Source7  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.0/commons-logging-1.0.pom
Source8  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.jar
Source9  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.pom
Source10  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.1/commons-logging-1.1.jar
Source11  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.1/commons-logging-1.1.pom
Source12  : https://repo1.maven.org/maven2/commons-logging/commons-logging/1.2/commons-logging-1.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-1.1
Requires: mvn-commons-logging-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-logging package.
Group: Data

%description data
data components for the mvn-commons-logging package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0.3
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0.4
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.1.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.1.1
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.1
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.2
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/commons-logging/g/1.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/i/1.1
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/commons-logging/i/1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-logging/i/1.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/commons-logging/i/1.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/commons-logging/g/1.0.3/commons-logging-1.0.3.jar
/usr/share/java/.m2/repository/commons-logging/g/1.0.3/commons-logging-api-1.1.jar
/usr/share/java/.m2/repository/commons-logging/g/1.0.4/commons-logging-1.0.3.pom
/usr/share/java/.m2/repository/commons-logging/g/1.0.4/commons-logging-api-1.1.pom
/usr/share/java/.m2/repository/commons-logging/g/1.0/commons-logging-1.0.4.jar
/usr/share/java/.m2/repository/commons-logging/g/1.0/commons-logging-1.0.4.pom
/usr/share/java/.m2/repository/commons-logging/g/1.1.1/commons-logging-1.0.jar
/usr/share/java/.m2/repository/commons-logging/g/1.1.1/commons-logging-1.0.pom
/usr/share/java/.m2/repository/commons-logging/g/1.1/commons-logging-1.1.1.jar
/usr/share/java/.m2/repository/commons-logging/g/1.1/commons-logging-1.1.1.pom
/usr/share/java/.m2/repository/commons-logging/g/1.2/commons-logging-1.1.jar
/usr/share/java/.m2/repository/commons-logging/i/1.1/commons-logging-1.1.pom
/usr/share/java/.m2/repository/commons-logging/i/1.1/commons-logging-1.2.pom
