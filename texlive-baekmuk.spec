%global tl_name baekmuk
%global tl_revision 56915

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2.1
Release:	%{tl_revision}.1
Summary:	Baekmuk Korean TrueType fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/baekmuk
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/baekmuk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/baekmuk.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle consists of four Korean fonts: batang.ttf: serif dotum.ttf:
sans-serif gulim.ttf: sans-serif (rounded) hline.ttf: headline These
fonts were originally retrieved from http://kldp.net/baekmuk/ and are no
longer maintained.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/doc/fonts/baekmuk
%dir %{_datadir}/texmf-dist/fonts/truetype/public
%dir %{_datadir}/texmf-dist/fonts/truetype/public/baekmuk
%doc %{_datadir}/texmf-dist/doc/fonts/baekmuk/COPYRIGHT
%doc %{_datadir}/texmf-dist/doc/fonts/baekmuk/COPYRIGHT.ks
%doc %{_datadir}/texmf-dist/doc/fonts/baekmuk/README.md
%{_datadir}/texmf-dist/fonts/truetype/public/baekmuk/batang.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/baekmuk/dotum.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/baekmuk/gulim.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/baekmuk/hline.ttf
