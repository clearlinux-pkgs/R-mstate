#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mstate
Version  : 0.2.11
Release  : 6
URL      : https://cran.r-project.org/src/contrib/mstate_0.2.11.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mstate_0.2.11.tar.gz
Summary  : Data Preparation, Estimation and Prediction in Multi-State
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mstate-lib
Requires: R-RColorBrewer
Requires: R-cmprsk
BuildRequires : R-RColorBrewer
BuildRequires : R-cmprsk
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-mstate package.
Group: Libraries

%description lib
lib components for the R-mstate package.


%prep
%setup -q -c -n mstate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530404868

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530404868
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mstate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mstate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mstate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mstate|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mstate/CITATION
/usr/lib64/R/library/mstate/DESCRIPTION
/usr/lib64/R/library/mstate/INDEX
/usr/lib64/R/library/mstate/Meta/Rd.rds
/usr/lib64/R/library/mstate/Meta/data.rds
/usr/lib64/R/library/mstate/Meta/features.rds
/usr/lib64/R/library/mstate/Meta/hsearch.rds
/usr/lib64/R/library/mstate/Meta/links.rds
/usr/lib64/R/library/mstate/Meta/nsInfo.rds
/usr/lib64/R/library/mstate/Meta/package.rds
/usr/lib64/R/library/mstate/Meta/vignette.rds
/usr/lib64/R/library/mstate/NAMESPACE
/usr/lib64/R/library/mstate/R/mstate
/usr/lib64/R/library/mstate/R/mstate.rdb
/usr/lib64/R/library/mstate/R/mstate.rdx
/usr/lib64/R/library/mstate/data/aidssi.RData
/usr/lib64/R/library/mstate/data/aidssi2.RData
/usr/lib64/R/library/mstate/data/bmt.RData
/usr/lib64/R/library/mstate/data/ebmt1.RData
/usr/lib64/R/library/mstate/data/ebmt2.RData
/usr/lib64/R/library/mstate/data/ebmt3.RData
/usr/lib64/R/library/mstate/data/ebmt4.RData
/usr/lib64/R/library/mstate/data/prothr.RData
/usr/lib64/R/library/mstate/doc/Tutorial.R
/usr/lib64/R/library/mstate/doc/Tutorial.Rnw
/usr/lib64/R/library/mstate/doc/Tutorial.pdf
/usr/lib64/R/library/mstate/doc/index.html
/usr/lib64/R/library/mstate/help/AnIndex
/usr/lib64/R/library/mstate/help/aliases.rds
/usr/lib64/R/library/mstate/help/mstate.rdb
/usr/lib64/R/library/mstate/help/mstate.rdx
/usr/lib64/R/library/mstate/help/paths.rds
/usr/lib64/R/library/mstate/html/00Index.html
/usr/lib64/R/library/mstate/html/R.css
/usr/lib64/R/library/mstate/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mstate/libs/mstate.so
/usr/lib64/R/library/mstate/libs/mstate.so.avx2
/usr/lib64/R/library/mstate/libs/mstate.so.avx512
