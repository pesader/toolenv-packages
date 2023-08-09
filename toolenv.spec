Name:           toolenv
Version:        0.1.0
Release:        1%{?dist}
Summary:        A simple utility to manage toolbx environments
BuildArch:      noarch

License:        GPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       bash

%description

%prep
%autosetup

%install
rm -rf $RPM_BUILD_ROOT

# Instal toolenv script
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp %{name} $RPM_BUILD_ROOT%{_bindir}

# Instal toolenv configuration
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
cp %{name}.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

%files
%{_bindir}/%{name}
%{_sysconfdir}/profile.d/%{name}.sh

%changelog
* Sun Aug 06 2023 pesader <pedro.saderazevedo@pm.me>
- First version packaged
