using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Machine.Specifications;

namespace ClassLibrary1
{
    [Subject("Evolver")]
    public class EvolvingAnEmptyGrid : BaseContext
    {
        
        It returns_an_empty_grid = () =>
            {
                grid = CreateGrid();
                Evolve(grid).ShouldEqual(grid);

            };

        
        
    }
}
