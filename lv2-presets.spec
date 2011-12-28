Summary:	LV2 Presets extension - presets for LV2 plugins
Summary(pl.UTF-8):	Rozszerzenie LV2 Presets - ustawienia predefiniowane dla wtyczek LV2
Name:		lv2-presets
Version:	2.2
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	2579bd395f3a4f5145a776b690d2caf8
URL:		http://lv2plug.in/ns/ext/presets/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
Requires:	lv2core >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 Presets extension describes a format for presets (i.e. named sets
of control values) for LV2 plugins.

%description -l pl.UTF-8
Rozszerzenie LV2 Presets opisuje format predefiniowanych ustawień
(tzn. nazwanych zbiorów wartości kontrolnych) dla wtyczek LV2.

%package devel
Summary:	Development files for LV2 Presets extension
Summary(pl.UTF-8):	Pliki programistyczne rozszerzenia LV2 Presets
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core-devel >= 6.0

%description devel
Development files for LV2 Presets extension.

%description devel -l pl.UTF-8
Pliki programistyczne rozszerzenia LV2 Presets.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%dir %{_libdir}/lv2/presets.lv2
%{_libdir}/lv2/presets.lv2/presets.ttl
%{_libdir}/lv2/presets.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
#%{_libdir}/lv2/presets.lv2/presets.h
%{_includedir}/lv2/lv2plug.in/ns/ext/presets
%{_pkgconfigdir}/lv2-lv2plug.in-ns-ext-presets.pc
