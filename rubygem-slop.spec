#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-slop
Version  : 4.4.1
Release  : 13
URL      : https://rubygems.org/downloads/slop-4.4.1.gem
Source0  : https://rubygems.org/downloads/slop-4.4.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
Slop
====
Slop is a simple option parser with an easy to remember syntax and friendly API.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n slop-4.4.1
gem spec %{SOURCE0} -l --ruby > rubygem-slop.gemspec

%build
export LANG=C
gem build rubygem-slop.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
slop-4.4.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/slop-4.4.1
ruby -v -I.:lib:test test*/test_*.rb
ruby -v -I.:lib:test test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/slop-4.4.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/lib/slop.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/lib/slop/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/lib/slop/option.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/lib/slop/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/lib/slop/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/lib/slop/result.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/lib/slop/types.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/slop.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/test/error_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/test/option_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/test/options_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/test/parser_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/test/result_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/test/slop_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/slop-4.4.1/test/types_test.rb
/usr/lib64/ruby/gems/2.3.0/specifications/slop-4.4.1.gemspec
