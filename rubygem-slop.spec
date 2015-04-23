#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-slop
Version  : 3.6.0
Release  : 6
URL      : https://rubygems.org/downloads/slop-3.6.0.gem
Source0  : https://rubygems.org/downloads/slop-3.6.0.gem
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
API Documentation is available [here](http://leejarvis.github.com/rdoc/slop/).

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n slop-3.6.0
gem spec %{SOURCE0} -l --ruby > rubygem-slop.gemspec

%build
gem build rubygem-slop.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
slop-3.6.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/slop-3.6.0
ruby -I"lib:test" test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/slop-3.6.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/arguments-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/banner-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/cdesc-Commands.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/commands-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/default-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/execute_arguments%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/execute_global_opts%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/global-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/help-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/on-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/parse%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/present%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/to_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Commands/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Error/cdesc-Error.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/InvalidArgumentError/cdesc-InvalidArgumentError.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/InvalidCommandError/cdesc-InvalidCommandError.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/InvalidOptionError/cdesc-InvalidOptionError.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/MissingArgumentError/cdesc-MissingArgumentError.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/MissingOptionError/cdesc-MissingOptionError.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/accepts_optional_argument%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/argument_in_value-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/call-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/cdesc-Option.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/count-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/description-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/expects_argument%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/help-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/long-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/short-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/types-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/value%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/value-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/value_to_float-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/value_to_integer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/Option/value_to_range-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/add_callback-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/autocreate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/banner%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/banner-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/build_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/cdesc-Slop.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/clean-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/commands-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/commands_to_help-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/description%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/description-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/execute_multiple_switches-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/execute_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/extract_long_flag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/extract_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/extract_short_flag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/fetch_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/fetch_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/help-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/method_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/on-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/opt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/optspec-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/parse%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/parse%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/parse-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/present%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/process_item-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/respond_to_missing%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/separator-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/strict%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/to_h-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/to_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/Slop/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/slop-3.6.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/CHANGES.md
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/README.md
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/lib/slop.rb
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/lib/slop/commands.rb
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/lib/slop/option.rb
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/slop.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/test/commands_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/test/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/test/option_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/slop-3.6.0/test/slop_test.rb
/usr/lib64/ruby/gems/2.2.0/specifications/slop-3.6.0.gemspec
