%global pkg_name apache-commons-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global base_name       parent
%global short_name      commons-%{base_name}

Name:             %{?scl_prefix}%{pkg_name}
Version:          26
Release:          8.11%{?dist}
Summary:          Apache Commons Parent Pom
License:          ASL 2.0
URL:              http://svn.apache.org/repos/asf/commons/proper/%{short_name}/tags/%{short_name}-%{version}/

# svn export http://svn.apache.org/repos/asf/commons/proper/commons-parent/tags/commons-parent-26
# tar caf commons-parent-26.tar.xz commons-parent-26
Source0:          %{short_name}-%{version}.tar.xz

#common-build-plugin not in fedora yet
Patch1:           %{pkg_name}-remove-build-plugin.patch
BuildArch:        noarch

BuildRequires:    %{?scl_prefix_java_common}maven-local

BuildRequires:    maven30-mvn(org.apache:apache:pom:)
BuildRequires:    maven30-mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    maven30-mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    maven30-mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:    maven30-mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:    maven30-mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:    maven30-mvn(org.apache.rat:apache-rat-plugin)
BuildRequires:    maven30-mvn(org.codehaus.mojo:buildnumber-maven-plugin)

Requires:         maven30-mvn(org.codehaus.mojo:buildnumber-maven-plugin)


%description
The Project Object Model files for the apache-commons packages.

%prep
%setup -q -n %{short_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%patch1 -p0

%pom_xpath_remove "pom:profile[pom:id[text()='maven-3']]"
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 26-8.11
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 26-8.10
- Fix directory ownership

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-8.9
- Fix BR on apache-parent

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 26-8.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 26-8.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-8.7
- Mass rebuild 2014-05-26

* Fri Mar 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-8.6
- Remove maven 3 profile

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-8.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-8.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-8.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 26-8
- Mass rebuild 2013-12-27

* Thu Sep 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-7
- Add missing Requires: buildnumber-maven-plugin

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 26-6
- Migrate away from mvn-rpmbuild (Resolves: #997512)

* Mon Apr 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-5
- Add buildnumber-maven-plugin to R/BR

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-4
- Fix Requires and BuildRequires

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 26-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Oct 19 2012 Chris Spike <spike@fedoraproject.org> 22-4
- Updated to 26

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Alexander Kurtakov <akurtako@redhat.com> 22-2
- Add missing BR/R on buildbumber-maven-plugin.

* Wed Dec 7 2011 Alexander Kurtakov <akurtako@redhat.com> 22-1
- Update to latest upstream.

* Fri Apr 15 2011 Chris Spike <spike@fedoraproject.org> 20-1
- Updated to 20
- Fixed Rs for maven 3

* Sat Nov 6 2010 Chris Spike <spike@fedoraproject.org> 15-2
- Added patch to remove commons-build-plugin from pom file

* Wed Oct 20 2010 Chris Spike <spike@fedoraproject.org> 15-1
- Initial version of the package
