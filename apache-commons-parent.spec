%{?scl:%scl_package apache-%{short_name}}
%{!?scl:%global pkg_name %{name}}

%global short_name      commons-parent

Name:             %{?scl_prefix}apache-%{short_name}
Version:          42
Release:          3.2%{?dist}
Summary:          Apache Commons Parent Pom
License:          ASL 2.0
URL:              http://svn.apache.org/repos/asf/commons/proper/%{short_name}/tags/%{short_name}-%{version}/

# svn export http://svn.apache.org/repos/asf/commons/proper/commons-parent/tags/commons-parent-%{version}
# tar caf commons-parent-%{version}.tar.xz commons-parent-%{version}
Source0:          %{short_name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    %{?scl_prefix}maven-local
BuildRequires:    %{?scl_prefix}mvn(org.apache:apache:pom:)
BuildRequires:    %{?scl_prefix}mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    %{?scl_prefix}mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    %{?scl_prefix}mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:    %{?scl_prefix}mvn(org.codehaus.mojo:build-helper-maven-plugin)

Requires:         %{?scl_prefix}mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
The Project Object Model files for the apache-commons packages.

%prep
%setup -q -n %{short_name}-%{version}

# Plugin is not in fedora
%pom_remove_plugin org.apache.commons:commons-build-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

# Plugins useless in package builds
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin

# Remove profiles for plugins that are useless in package builds
for profile in animal-sniffer japicmp jacoco cobertura clirr; do
    %pom_xpath_remove "pom:profile[pom:id='$profile']"
done

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 42-3.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 42-3.1
- Automated package import and SCL-ization

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 42-3
- Remove more useless plugins

* Thu Jan 05 2017 Michael Simacek <msimacek@redhat.com> - 42-2
- Remove profiles for plugins that are useless in package builds

* Mon Jan 02 2017 Michael Simacek <msimacek@redhat.com> - 42-1
- Update to upstream version 42

* Tue Jun 14 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 40-2
- Add missing dependency

* Wed May 11 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 40-1
- Update to upstream version 40

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep  8 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 39-1
- Update to upstream version 39

* Thu Jun 25 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 38-1
- Update to upstream version 38

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb  3 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 37-2
- Remove animal-sniffer profile

* Mon Feb  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 37-1
- Update to upstream version 37

* Mon Oct 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 35-1
- Update to upstream version 35

* Wed Jul 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-4
- Fix build-requires on apache-parent

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-2
- Rebuild to regenerate Maven auto-requires

* Thu Apr 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-1
- Update to upstream version 34

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 33-2
- Remove maven 3 profile

* Wed Feb 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-1
- Update to upstream version 33

* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 32-2
- Remove use of maven-scm-publish-plugin plugin

* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 32-1
- Updated to latest upstream, rhbz #904731

* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 26-7
- Use pom macros instead of patching
- Update spec for latest guidelines rhbz #991975

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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
