using System;

namespace ClassLibrary1
{
    public class Grid
    {
        public override bool Equals(object obj)
        {

            return obj != null && this.GetHashCode() == obj.GetHashCode();

        }

        public override int GetHashCode()
        {
            return "".GetHashCode();
        }
    }
}