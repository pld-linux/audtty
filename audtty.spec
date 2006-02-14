Summary:	NCurses interface to Audacious media player
Summary(pl):	Interfejs ncurses do odtwarzacza multimedialnego Audacious
Name:		audtty
Version:	0.1.3
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.nenolod.net/audtool/%{name}-%{version}.tar.bz2
# Source0-md5:	d0346950d1c9e58635de1b89c83f9eb7
URL:		http://audacious-media-player.org/Audtty
BuildRequires:	audacious-devel
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audtty is an ncurses-based client for Audacious media player.

%description -l pl
Audtty to oparty na ncurses klient odtwarzacza multimedialnego
Audacious.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
