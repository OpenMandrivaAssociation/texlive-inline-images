Name:		texlive-inline-images
Version:	61719
Release:	2
Summary:	Inline images in base64 encoding
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/inline-images
License:	lgpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inline-images.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inline-images.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a command \inlineimg to dynamically create
a file containing the inline image in base64 format, which is
decoded and included in the source file. Requirements LaTeX
must be run with option --shell-escape. Program base64.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/inline-images
%doc %{_texmfdistdir}/doc/latex/inline-images

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
