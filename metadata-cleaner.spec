Summary:	A Python GTK application to view and clean metadata in files using mat2 
Name:		metadata-cleaner
Version:	2.2.5
Release:	1
License:	GPLv3+ and CC-BY-SA
Group:		File tools
URL:		https://metadatacleaner.romainvigier.fr
Source0:	https://gitlab.com/rmnvgr/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	appstream
BuildRequires:	mat2
BuildRequires:	meson
BuildRequires:	itstool
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	python3dist(setuptools)

Requires:	mat2
#Requires:	typelib(Adw)

%description
Metadata within a file can tell a lot about you. Cameras record data
about when and where a picture was taken and which camera was used.
Office applications automatically add author and company information
to documents and spreadsheets.  This is sensitive information and you
may not want to disclose it.

This tool allows you to view metadata in your files and to get rid of
it, as much as possible.

Under the hood, it relies on mat2 to parse and remove the metadata.

%files -f %{name}.lang
%license LICENSE.md
%doc CHANGELOG.md CONTRIBUTING.md README.md RELEASING.md
%{_bindir}/%{name}
%{py_sitedir}/metadatacleaner/
%{_datadir}/%{name}/*
%{_datadir}/help/*
%{_datadir}/dbus-1/services/fr.romainvigier.MetadataCleaner.service
%{_datadir}/glib-2.0/schemas/fr.romainvigier.MetadataCleaner.gschema.xml
%{_datadir}/applications/fr.romainvigier.MetadataCleaner.desktop
%{_datadir}/metainfo/fr.romainvigier.MetadataCleaner.metainfo.xml
%{_iconsdir}/hicolor/*/apps/*.svg

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

# localization
%find_lang %{name} --all-name

