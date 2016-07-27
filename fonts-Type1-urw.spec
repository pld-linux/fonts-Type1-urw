%define	pre	pre44
Summary:	Free versions of the 35 standard PostScript fonts
Summary(pl.UTF-8):	Wolnodostępne wersje 35 standardowych fontów postscriptowych
Name:		fonts-Type1-urw
Version:	1.0.7
Release:	0.%{pre}.1
License:	GPL v2
Group:		Fonts
Source0:	https://distfiles.macports.org/urw-fonts/urw-fonts-%{version}%{pre}.tar.bz2
# Source0-md5:	51c6c2690593cd9bd92f197a6f2ff8bd
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
%{t1fontsdir}/a0100??l.pfb
%{t1fontsdir}/b0180??l.pfb
%{t1fontsdir}/c0590??l.pfb
%{t1fontsdir}/d050000l.pfb
%{t1fontsdir}/n0190??l.pfb
%{t1fontsdir}/n0210??l.pfb
%{t1fontsdir}/n0220??l.pfb
%{t1fontsdir}/p0520??l.pfb
%{t1fontsdir}/s050000l.pfb
%{t1fontsdir}/z003034l.pfb
%{t1afmdir}/a0100??l.afm
%{t1afmdir}/b0180??l.afm
%{t1afmdir}/c0590??l.afm
%{t1afmdir}/d050000l.afm
%{t1afmdir}/n0190??l.afm
%{t1afmdir}/n0210??l.afm
%{t1afmdir}/n0220??l.afm
%{t1afmdir}/p0520??l.afm
%{t1afmdir}/s050000l.afm
%{t1afmdir}/z003034l.afm
%{t1pfmdir}/a0100??l.pfm
%{t1pfmdir}/b0180??l.pfm
%{t1pfmdir}/c0590??l.pfm
%{t1pfmdir}/d050000l.pfm
%{t1pfmdir}/n0190??l.pfm
%{t1pfmdir}/n0210??l.pfm
%{t1pfmdir}/n0220??l.pfm
%{t1pfmdir}/p0520??l.pfm
%{t1pfmdir}/s050000l.pfm
%{t1pfmdir}/z003034l.pfm
