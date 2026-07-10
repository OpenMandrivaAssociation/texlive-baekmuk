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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle consists of four Korean fonts: batang.ttf: serif dotum.ttf:
sans-serif gulim.ttf: sans-serif (rounded) hline.ttf: headline These
fonts were originally retrieved from http://kldp.net/baekmuk/ and are no
longer maintained.

