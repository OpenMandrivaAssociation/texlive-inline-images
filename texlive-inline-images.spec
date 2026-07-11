%global tl_name inline-images
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Inline images in base64 encoding
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/inline-images
License:	lgpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inline-images.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inline-images.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a command \inlineimg to dynamically create a file
containing the inline image in base64 format, which is decoded and
included in the source file. Requirements LaTeX must be run with option
--shell-escape. Program base64.

