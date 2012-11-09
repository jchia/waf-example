#include <myproj/foo/Foo.hpp>
#include <myproj/bar/Bar.hpp>

namespace myproj {
namespace bar {

int Bar::calc(int x) {
    foo::Foo foo;
    return foo.calc(x) + foo.calc(x + 1);
}

} } // myproj::foo
