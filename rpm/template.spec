%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-velodyne-pointcloud
Version:        2.5.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS velodyne_pointcloud package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       pcl-devel
Requires:       ros-jazzy-angles
Requires:       ros-jazzy-diagnostic-updater
Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-message-filters
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-components
Requires:       ros-jazzy-sensor-msgs
Requires:       ros-jazzy-tf2
Requires:       ros-jazzy-tf2-ros
Requires:       ros-jazzy-velodyne-msgs
Requires:       yaml-cpp-devel
Requires:       ros-jazzy-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  pcl-devel
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-angles
BuildRequires:  ros-jazzy-diagnostic-updater
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-message-filters
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-components
BuildRequires:  ros-jazzy-sensor-msgs
BuildRequires:  ros-jazzy-tf2
BuildRequires:  ros-jazzy-tf2-ros
BuildRequires:  ros-jazzy-velodyne-msgs
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-gtest
BuildRequires:  ros-jazzy-ament-index-cpp
BuildRequires:  ros-jazzy-ament-lint-auto
BuildRequires:  ros-jazzy-ament-lint-common
%endif

%description
Point cloud conversions for Velodyne 3D LIDARs.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Thu Dec 19 2024 Josh Whitley <whitleysoftwareservices@gmail.com> - 2.5.1-1
- Autogenerated by Bloom

* Fri Jun 14 2024 Josh Whitley <whitleysoftwareservices@gmail.com> - 2.4.0-1
- Autogenerated by Bloom

* Fri Apr 19 2024 Josh Whitley <whitleysoftwareservices@gmail.com> - 2.3.0-4
- Autogenerated by Bloom

* Wed Mar 06 2024 Josh Whitley <whitleysoftwareservices@gmail.com> - 2.3.0-3
- Autogenerated by Bloom

