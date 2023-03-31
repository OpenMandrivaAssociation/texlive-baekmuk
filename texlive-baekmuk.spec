Name:		texlive-baekmuk
Version:	56915
Release:	2
Summary:	Baekmuk Korean TrueType fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/baekmuk
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/baekmuk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/baekmuk.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle consists of four Korean fonts: batang.ttf: serif
dotum.ttf: sans-serif gulim.ttf: sans-serif (rounded)
hline.ttf: headline These fonts were originally retrieved from
http://kldp.net/baekmuk/ and are no longer maintained.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/public/baekmuk
%doc %{_texmfdistdir}/doc/fonts/baekmuk

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
