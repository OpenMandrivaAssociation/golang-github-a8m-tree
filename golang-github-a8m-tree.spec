# Run tests in check section
%bcond_without check

%global goipath         github.com/a8m/tree
%global commit          3cf936ce15d6100c49d9c75f79c220ae7e579599

%global common_description %{expand:
An implementation of the tree command written in Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        An implementation of the tree command written in Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%build  
%gobuildroot
%gobuild -o _bin/tree %{goipath}/cmd/tree


%install
%goinstall
install -Dpm 0755 _bin/tree %{buildroot}%{_bindir}/gotree


%if %{with check}
%check
%gochecks
%endif


%files
%license LICENSE
%{_bindir}/gotree


%files devel -f devel.file-list
%doc README.md
%license LICENSE


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git3cf936c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180422gitcf42b1e
- First package for Fedora

