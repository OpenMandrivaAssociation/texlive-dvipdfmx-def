# revision 32770
# category Package
# catalog-ctan /macros/latex/contrib/dvipdfmx-def/dvipdfmx.def
# catalog-date 2013-09-22 08:58:08 +0200
# catalog-license lppl
# catalog-version 3.3
Epoch:		1
Name:		texlive-dvipdfmx-def
Version:	3.3
Release:	2
Summary:	Configuration file for dvipdfmx graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dvipdfmx-def/dvipdfmx.def
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipdfmx-def.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is the graphics driver for use when output is to be
processed by dvipdfmx.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dvipdfmx-def/dvipdfmx.def

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
