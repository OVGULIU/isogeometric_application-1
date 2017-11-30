//
//   Project Name:        Kratos
//   Last Modified by:    $Author: hbui $
//   Date:                $Date: 5 Nov 2017 $
//   Revision:            $Revision: 1.0 $
//
//

#if !defined(KRATOS_ISOGEOMETRIC_APPLICATION_CONTROL_GRID_H_INCLUDED )
#define  KRATOS_ISOGEOMETRIC_APPLICATION_CONTROL_GRID_H_INCLUDED

// System includes
#include <vector>

// External includes

// Project includes
#include "includes/define.h"

namespace Kratos
{

/**
This class is an abstract container to keep the control values.
TODO implement iterator to iterate through control values.
 */
template<typename TDataType>
class ControlGrid
{
public:
    /// Pointer definition
    KRATOS_CLASS_POINTER_DEFINITION(ControlGrid);

    /// Type definition
    typedef TDataType DataType;

    /// Default constructor
    ControlGrid() : mName("UNKNOWN") {}

    /// Constructor with name
    ControlGrid(const std::string& Name) : mName(Name) {}

    /// Destructor
    virtual ~ControlGrid() {}

    /// Create a new control grid pointer
    static ControlGrid::Pointer Create() {return ControlGrid::Pointer(new ControlGrid());}

    /// Clone this grid function
    virtual typename ControlGrid<TDataType>::Pointer Clone() const {return NULL;}

    /// Set the name
    void SetName(const std::string& Name) {mName = Name;}

    /// Get the name
    const std::string& Name() const {return mName;}

    /// Get the size of underlying data
    virtual std::size_t Size() const
    {
        KRATOS_THROW_ERROR(std::logic_error, "Error calling base class function", __FUNCTION__)
    }

    /// Get the size of underlying data
    virtual std::size_t size() const
    {
        KRATOS_THROW_ERROR(std::logic_error, "Error calling base class function", __FUNCTION__)
    }

    /// Get the data at specific point
    virtual const TDataType& GetData(const std::size_t& i) const
    {
        KRATOS_THROW_ERROR(std::logic_error, "Error calling base class function", __FUNCTION__)
    }

    /// Set the data at specific point
    /// Be careful with this method. You can destroy the coherency of internal data.
    virtual void SetData(const std::size_t& i, const TDataType& value)
    {
        KRATOS_THROW_ERROR(std::logic_error, "Error calling base class function", __FUNCTION__)
    }

    /// overload operator []
    virtual TDataType& operator[] (const std::size_t& i)
    {
        KRATOS_THROW_ERROR(std::logic_error, "Error calling base class function", __FUNCTION__)
    }

    /// overload operator []
    virtual const TDataType& operator[] (const std::size_t& i) const
    {
        KRATOS_THROW_ERROR(std::logic_error, "Error calling base class function", __FUNCTION__)
    }

    // /// extract the sub grid, given local indices of the control values
    // void ControlGrid::Pointer ExtractSubGrid(const std::vector<std::size_t>& local_ids) const
    // {
    //     ControlGrid::Pointer pSubControlGrid = Create();
    //     for (std::size_t i = 0; i < local_ids.size(); ++i)
    //     {

    //     }
    //     return pSubControlGrid;
    // }

    /// Information
    virtual void PrintInfo(std::ostream& rOStream) const
    {
        rOStream << "Control Grid " << Name() << "[" << Size() << "]";
    }

    virtual void PrintData(std::ostream& rOStream) const
    {
    }

private:

    std::string mName;
};

/// output stream function
template<typename TDataType>
inline std::ostream& operator <<(std::ostream& rOStream, const ControlGrid<TDataType>& rThis)
{
    rThis.PrintInfo(rOStream);
    rOStream << std::endl;
    rThis.PrintData(rOStream);
    return rOStream;
}

} // namespace Kratos.

#endif // KRATOS_ISOGEOMETRIC_APPLICATION_CONTROL_GRID_H_INCLUDED defined
