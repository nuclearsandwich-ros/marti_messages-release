Name:           ros-indigo-marti-sensor-msgs
Version:        0.7.0
Release:        0%{?dist}
Summary:        ROS marti_sensor_msgs package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_messages
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation

%description
marti_sensor_msgs

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Oct 09 2018 Marc Alban <malban@swri.org> - 0.7.0-0
- Autogenerated by Bloom

* Thu May 24 2018 Marc Alban <malban@swri.org> - 0.6.0-0
- Autogenerated by Bloom

* Thu Apr 05 2018 Marc Alban <malban@swri.org> - 0.5.0-0
- Autogenerated by Bloom

* Wed Nov 08 2017 Marc Alban <malban@swri.org> - 0.4.0-0
- Autogenerated by Bloom

* Thu Sep 28 2017 Marc Alban <malban@swri.org> - 0.3.0-0
- Autogenerated by Bloom

* Tue Aug 29 2017 Marc Alban <malban@swri.org> - 0.2.0-0
- Autogenerated by Bloom

* Tue Aug 15 2017 Marc Alban <malban@swri.org> - 0.1.0-0
- Autogenerated by Bloom

* Mon May 08 2017 Marc Alban <malban@swri.org> - 0.0.9-0
- Autogenerated by Bloom

* Sat Mar 18 2017 Marc Alban <malban@swri.org> - 0.0.8-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Marc Alban <malban@swri.org> - 0.0.7-0
- Autogenerated by Bloom

* Sun Oct 23 2016 Marc Alban <malban@swri.org> - 0.0.6-0
- Autogenerated by Bloom

* Sun Aug 14 2016 Marc Alban <malban@swri.org> - 0.0.5-0
- Autogenerated by Bloom

* Fri May 20 2016 Marc Alban <malban@swri.org> - 0.0.4-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Marc Alban <malban@swri.org> - 0.0.3-0
- Autogenerated by Bloom

* Fri Mar 04 2016 Marc Alban <malban@swri.org> - 0.0.2-0
- Autogenerated by Bloom

* Wed Sep 23 2015 Marc Alban <malban@swri.org> - 0.0.1-1
- Autogenerated by Bloom

* Wed Sep 23 2015 Marc Alban <malban@swri.org> - 0.0.1-0
- Autogenerated by Bloom

