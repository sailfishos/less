Name:       less
Summary:    A text file browser similar to more, but better
Version:    608
Release:    1
License:    GPLv3+ or BSD
URL:        http://www.greenwoodsoftware.com/less/
Source0:    %{name}-%{version}.tar.gz
Source1:    lesspipe.sh
Source2:    less.sh
Source3:    less.csh
Patch1: less-394-time.patch
Patch2: less-475-fsync.patch
Patch3: less-458-lessecho-usage.patch
Patch4: less-458-lesskey-usage.patch
Patch5: less-458-old-bot-in-help.patch
Patch6: less-608-disable-man.patch
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
The less utility is a text file browser that resembles more, but has
more capabilities.  Less allows you to move backwards in the file as
well as forwards.  Since less doesn't have to read the entire input file
before it starts, less starts up more quickly than text editors (for
example, vi).

You should install less because it is a basic utility for viewing text
files, and you'll use it frequently.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build

autoreconf -vif
%configure
%make_build -f Makefile.aut

%install
%make_install

mkdir -p $RPM_BUILD_ROOT/etc/profile.d
install -p -c -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}
install -p -c -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d
install -p -c -m 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/profile.d
ls -la $RPM_BUILD_ROOT/etc/profile.d

%files
%defattr(-,root,root,-)
%license LICENSE COPYING
%{_sysconfdir}/profile.d/*
%{_bindir}/*
