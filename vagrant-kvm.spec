Summary:	Vagrant Plugin to add KVM provider to Vagrant
Name:		vagrant-kvm
Version:	0.1.1
Release:	0.1
License:	MIT
Group:		Applications/Emulators
Source0:	https://github.com/adrahon/vagrant-kvm/tarball/master?/%{name}-44e7eb1.tgz
# Source0-md5:	ea30e020c8fef19c6100738c71e8dec0
URL:		https://github.com/adrahon/vagrant-kvm
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-libvirt >= 0.4.0
Requires:	ruby-nokogiri >= 1.5.6
Requires:	ruby-rubygems >= 1.3.6
Requires:	vagrant >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		vagrantdir	%{_datadir}/vagrant

%description
A Vagrant 1.1+ plugin that adds a KVM provider to Vagrant, allowing
Vagrant to control and provision KVM/QEMU VM.

%prep
%setup -qc
mv adrahon-vagrant-kvm-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md LICENSE
%{ruby_vendorlibdir}/vagrant-kvm.rb
%{ruby_vendorlibdir}/vagrant-kvm
