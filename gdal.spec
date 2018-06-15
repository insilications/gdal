#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gdal
Version  : 2.2.3
Release  : 6
URL      : http://download.osgeo.org/gdal/2.2.3/gdal-2.2.3.tar.xz
Source0  : http://download.osgeo.org/gdal/2.2.3/gdal-2.2.3.tar.xz
Summary  : Geospatial Data Abstraction Library
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause LGPL-2.0 Libpng MIT Public-Domain Qhull
Requires: gdal-bin
Requires: gdal-config
Requires: gdal-lib
Requires: gdal-data
BuildRequires : curl-dev
BuildRequires : hdf5-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libxml2-dev
BuildRequires : pbr
BuildRequires : pcre-dev
BuildRequires : pip
BuildRequires : pkgconfig(bash-completion)

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zlib-dev

%description
The .i files in this directory are generated files and should not be edited
manually.

%package bin
Summary: bin components for the gdal package.
Group: Binaries
Requires: gdal-data
Requires: gdal-config

%description bin
bin components for the gdal package.


%package config
Summary: config components for the gdal package.
Group: Default

%description config
config components for the gdal package.


%package data
Summary: data components for the gdal package.
Group: Data

%description data
data components for the gdal package.


%package dev
Summary: dev components for the gdal package.
Group: Development
Requires: gdal-lib
Requires: gdal-bin
Requires: gdal-data
Provides: gdal-devel

%description dev
dev components for the gdal package.


%package lib
Summary: lib components for the gdal package.
Group: Libraries
Requires: gdal-data

%description lib
lib components for the gdal package.


%prep
%setup -q -n gdal-2.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1516667177
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1516667177
rm -rf %{buildroot}
%make_install
## make_install_append content
install -D %{buildroot}/usr/etc/bash_completion.d/gdal-bash-completion.sh %{buildroot}/usr/share/bash-completion/completions/gdal-bash-completion.sh
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gdal-config
/usr/bin/gdal_contour
/usr/bin/gdal_grid
/usr/bin/gdal_rasterize
/usr/bin/gdal_translate
/usr/bin/gdaladdo
/usr/bin/gdalbuildvrt
/usr/bin/gdaldem
/usr/bin/gdalenhance
/usr/bin/gdalinfo
/usr/bin/gdallocationinfo
/usr/bin/gdalmanage
/usr/bin/gdalserver
/usr/bin/gdalsrsinfo
/usr/bin/gdaltindex
/usr/bin/gdaltransform
/usr/bin/gdalwarp
/usr/bin/gnmanalyse
/usr/bin/gnmmanage
/usr/bin/nearblack
/usr/bin/ogr2ogr
/usr/bin/ogrinfo
/usr/bin/ogrlineref
/usr/bin/ogrtindex
/usr/bin/testepsg

%files config
%defattr(-,root,root,-)
%exclude /usr/etc/bash_completion.d/gdal-bash-completion.sh

%files data
%defattr(-,root,root,-)
/usr/share/GDALLogoBW.svg
/usr/share/GDALLogoColor.svg
/usr/share/GDALLogoGS.svg
/usr/share/LICENSE.TXT
/usr/share/bash-completion/completions/gdal-bash-completion.sh
/usr/share/compdcs.csv
/usr/share/coordinate_axis.csv
/usr/share/cubewerx_extra.wkt
/usr/share/datum_shift.csv
/usr/share/default.rsc
/usr/share/ecw_cs.wkt
/usr/share/ellipsoid.csv
/usr/share/epsg.wkt
/usr/share/esri_StatePlane_extra.wkt
/usr/share/esri_Wisconsin_extra.wkt
/usr/share/esri_extra.wkt
/usr/share/gcs.csv
/usr/share/gcs.override.csv
/usr/share/gdal_datum.csv
/usr/share/gdalicon.png
/usr/share/gdalvrt.xsd
/usr/share/geoccs.csv
/usr/share/gml_registry.xml
/usr/share/gmlasconf.xml
/usr/share/gmlasconf.xsd
/usr/share/gt_datum.csv
/usr/share/gt_ellips.csv
/usr/share/header.dxf
/usr/share/inspire_cp_BasicPropertyUnit.gfs
/usr/share/inspire_cp_CadastralBoundary.gfs
/usr/share/inspire_cp_CadastralParcel.gfs
/usr/share/inspire_cp_CadastralZoning.gfs
/usr/share/jpfgdgml_AdmArea.gfs
/usr/share/jpfgdgml_AdmBdry.gfs
/usr/share/jpfgdgml_AdmPt.gfs
/usr/share/jpfgdgml_BldA.gfs
/usr/share/jpfgdgml_BldL.gfs
/usr/share/jpfgdgml_Cntr.gfs
/usr/share/jpfgdgml_CommBdry.gfs
/usr/share/jpfgdgml_CommPt.gfs
/usr/share/jpfgdgml_Cstline.gfs
/usr/share/jpfgdgml_ElevPt.gfs
/usr/share/jpfgdgml_GCP.gfs
/usr/share/jpfgdgml_LeveeEdge.gfs
/usr/share/jpfgdgml_RailCL.gfs
/usr/share/jpfgdgml_RdASL.gfs
/usr/share/jpfgdgml_RdArea.gfs
/usr/share/jpfgdgml_RdCompt.gfs
/usr/share/jpfgdgml_RdEdg.gfs
/usr/share/jpfgdgml_RdMgtBdry.gfs
/usr/share/jpfgdgml_RdSgmtA.gfs
/usr/share/jpfgdgml_RvrMgtBdry.gfs
/usr/share/jpfgdgml_SBAPt.gfs
/usr/share/jpfgdgml_SBArea.gfs
/usr/share/jpfgdgml_SBBdry.gfs
/usr/share/jpfgdgml_WA.gfs
/usr/share/jpfgdgml_WL.gfs
/usr/share/jpfgdgml_WStrA.gfs
/usr/share/jpfgdgml_WStrL.gfs
/usr/share/netcdf_config.xsd
/usr/share/nitf_spec.xml
/usr/share/nitf_spec.xsd
/usr/share/ogrvrt.xsd
/usr/share/osmconf.ini
/usr/share/ozi_datum.csv
/usr/share/ozi_ellips.csv
/usr/share/pci_datum.txt
/usr/share/pci_ellips.txt
/usr/share/pcs.csv
/usr/share/pcs.override.csv
/usr/share/plscenesconf.json
/usr/share/prime_meridian.csv
/usr/share/projop_wparm.csv
/usr/share/ruian_vf_ob_v1.gfs
/usr/share/ruian_vf_st_uvoh_v1.gfs
/usr/share/ruian_vf_st_v1.gfs
/usr/share/ruian_vf_v1.gfs
/usr/share/s57agencies.csv
/usr/share/s57attributes.csv
/usr/share/s57expectedinput.csv
/usr/share/s57objectclasses.csv
/usr/share/seed_2d.dgn
/usr/share/seed_3d.dgn
/usr/share/stateplane.csv
/usr/share/trailer.dxf
/usr/share/unit_of_measure.csv
/usr/share/vdv452.xml
/usr/share/vdv452.xsd
/usr/share/vertcs.csv
/usr/share/vertcs.override.csv

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libgdal.so
/usr/lib64/pkgconfig/gdal.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgdal.so.20
/usr/lib64/libgdal.so.20.3.2
