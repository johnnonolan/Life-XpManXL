using Machine.Specifications;

namespace ClassLibrary1
{
    public class BaseContext
    {

        Establish context = () => grid = CreateGrid();

        protected static Grid Evolve(Grid emptyGrid)
        {
            return CreateGrid();
        }

        protected static Grid CreateGrid()
        {
            return new Grid();
        }

        protected static Grid grid;
    }
}