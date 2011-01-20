using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Machine.Specifications;

namespace ClassLibrary1
{
    [Subject("Evolving")]
    public class EvolvingASingleCellGrid : BaseContext
    {
        Establish that = () =>
            {
                grid.Add(new
                             {
                             });
        Because of = () => grid = Evolve(grid);
        It returns_an_empty_grid = () => grid.ShouldEqual(grid);
    
    }
}
