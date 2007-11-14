%define	pre	pre43
Summary:	Free versions of the 35 standard PostScript fonts
Name:		fonts-Type1-urw
Version:	1.0.7
Release:	0.%{pre}.2
License:	GPL
Group:		Fonts
Source0:	ftp://ftp.gnome.ru/fonts/urw/release/urw-fonts-%{version}%{pre}.tar.bz2
# Source0-md5:	97ff7f315bcf36558d7f326878551ac3
BuildRequires:	xorg-app-mkfontscale
Requires(post,postun):	fontpostinst >= 0.1-6
Requires:	%{_fontsdir}/Type1
Obsoletes:	ghostscript-fonts-std
Provides:	ghostscript-fonts-std = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		t1fontsdir	%{_fontsdir}/Type1
%define		t1afmdir	%{t1fontsdir}/afm

%description
Free, good quality versions of the 35 standard PostScript(TM) fonts,
donated under the GPL by URW++ Design and Development GmbH. The
fonts.dir file font names match the original Adobe names of the fonts
(e.g., Times, Helvetica, etc.).

Install the urw-fonts package if you need free versions of standard
PostScript fonts.

%prep
%setup -q -c

%build
%{_bindir}/mkfontscale .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{t1fontsdir},%{t1afmdir}}

install *.pfb $RPM_BUILD_ROOT%{t1fontsdir}
install *.afm $RPM_BUILD_ROOT%{t1afmdir}

grep ".pfb" fonts.scale > $RPM_BUILD_ROOT%{t1fontsdir}/fonts.scale.urw

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc README*
%{t1fontsdir}/fonts.scale.urw
%{t1fontsdir}/*.pfb
%{t1afmdir}/*.afm
