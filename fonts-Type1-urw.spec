%define	pre	pre43
Summary:	Free versions of the 35 standard PostScript fonts
Summary(pl.UTF-8):	Wolnodostępne wersje 35 standardowych fontów postscriptowych
Name:		fonts-Type1-urw
Version:	1.0.7
Release:	0.%{pre}.4
License:	GPL v2
Group:		Fonts
Source0:	ftp://ftp.gnome.ru/fonts/urw/release/urw-fonts-%{version}%{pre}.tar.bz2
# Source0-md5:	97ff7f315bcf36558d7f326878551ac3
Source1:	%{name}.Fontmap
BuildRequires:	xorg-app-mkfontscale
Requires(post,postun):	fontpostinst >= 0.1-6
Requires:	%{_fontsdir}/Type1
Provides:	ghostscript-fonts-std
Obsoletes:	ghostscript-fonts-std
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		t1fontsdir	%{_fontsdir}/Type1
%define		t1afmdir	%{t1fontsdir}/afm
%define		t1pfmdir	%{t1fontsdir}/pfm

%description
Free, good quality versions of the 35 standard PostScript(TM) fonts,
donated under the GPL by URW++ Design and Development GmbH. The
fonts.dir file font names match the original Adobe names of the fonts
(e.g., Times, Helvetica, etc.).

%description -l pl.UTF-8
Wolnodostępne, dobrej jakości wersje 35 standardowych fontów
postscriptowych, wydanych na licencji GPL przez URW++ Design and
Development GmbH. Plik fonts.dir zawiera nazwy fontów pasujące do
oryginalnych nazw Adobe (np. Times, Helvetica itd.).

%prep
%setup -q -c

%build
%{_bindir}/mkfontscale .
tail -n +2 fonts.dir > fonts.dir.raw
LC_ALL=C sort -t- -k1,13 -u fonts.dir.raw > fonts.dir.sorted
join -j1 -t- -o1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,1.10,1.11,1.12,1.13,2.14,2.15 fonts.dir.sorted fonts.scale > fonts.scale.add
LC_ALL=C sort -u fonts.dir.raw fonts.scale.add > fonts.scale.urw

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{t1fontsdir},%{t1afmdir},%{t1pfmdir}}
cp -p *.pfb $RPM_BUILD_ROOT%{t1fontsdir}
cp -p *.afm $RPM_BUILD_ROOT%{t1afmdir}
cp -p *.pfm $RPM_BUILD_ROOT%{t1pfmdir}

cp -p fonts.scale.urw $RPM_BUILD_ROOT%{t1fontsdir}/fonts.scale.urw
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{t1fontsdir}/Fontmap.urw

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc README* ChangeLog
%{t1fontsdir}/Fontmap.urw
%{t1fontsdir}/fonts.scale.urw
%{t1fontsdir}/*.pfb
%{t1afmdir}/*.afm
%{t1pfmdir}/*.pfm
