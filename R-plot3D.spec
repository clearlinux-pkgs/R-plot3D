#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v4
# autospec commit: 213bb01
#
Name     : R-plot3D
Version  : 1.4.1
Release  : 20
URL      : https://cran.r-project.org/src/contrib/plot3D_1.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plot3D_1.4.1.tar.gz
Summary  : Plotting Multi-Dimensional Data
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: R-misc3d
BuildRequires : R-misc3d
BuildRequires : buildreq-R
BuildRequires : tcl
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n plot3D
pushd ..
cp -a plot3D buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707238410

%install
export SOURCE_DATE_EPOCH=1707238410
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/plot3D/DESCRIPTION
/usr/lib64/R/library/plot3D/INDEX
/usr/lib64/R/library/plot3D/Meta/Rd.rds
/usr/lib64/R/library/plot3D/Meta/data.rds
/usr/lib64/R/library/plot3D/Meta/features.rds
/usr/lib64/R/library/plot3D/Meta/hsearch.rds
/usr/lib64/R/library/plot3D/Meta/links.rds
/usr/lib64/R/library/plot3D/Meta/nsInfo.rds
/usr/lib64/R/library/plot3D/Meta/package.rds
/usr/lib64/R/library/plot3D/Meta/vignette.rds
/usr/lib64/R/library/plot3D/NAMESPACE
/usr/lib64/R/library/plot3D/R/plot3D
/usr/lib64/R/library/plot3D/R/plot3D.rdb
/usr/lib64/R/library/plot3D/R/plot3D.rdx
/usr/lib64/R/library/plot3D/data/Rdata.rdb
/usr/lib64/R/library/plot3D/data/Rdata.rds
/usr/lib64/R/library/plot3D/data/Rdata.rdx
/usr/lib64/R/library/plot3D/doc/index.html
/usr/lib64/R/library/plot3D/doc/plot3D.R
/usr/lib64/R/library/plot3D/doc/plot3D.pdf
/usr/lib64/R/library/plot3D/doc/plot3D.rnw
/usr/lib64/R/library/plot3D/doc/volcano.R
/usr/lib64/R/library/plot3D/doc/volcano.pdf
/usr/lib64/R/library/plot3D/doc/volcano.rnw
/usr/lib64/R/library/plot3D/help/AnIndex
/usr/lib64/R/library/plot3D/help/aliases.rds
/usr/lib64/R/library/plot3D/help/paths.rds
/usr/lib64/R/library/plot3D/help/plot3D.rdb
/usr/lib64/R/library/plot3D/help/plot3D.rdx
/usr/lib64/R/library/plot3D/html/00Index.html
/usr/lib64/R/library/plot3D/html/R.css
