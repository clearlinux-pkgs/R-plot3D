#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-plot3D
Version  : 1.4
Release  : 10
URL      : https://cran.r-project.org/src/contrib/plot3D_1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plot3D_1.4.tar.gz
Summary  : Plotting Multi-Dimensional Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-misc3d
BuildRequires : R-misc3d
BuildRequires : buildreq-R
BuildRequires : tcl

%description
No detailed description available

%prep
%setup -q -c -n plot3D
cd %{_builddir}/plot3D

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621868922

%install
export SOURCE_DATE_EPOCH=1621868922
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plot3D
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plot3D
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plot3D
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc plot3D || :


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
