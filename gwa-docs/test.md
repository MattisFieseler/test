@startuml

file "main"{
  () "startup"
}

file "HTMLServer"{
  class SimpleHTTPRequestHandler
  class HTMLServer{
    self.path
    do_GET()
  }

  () "run()"

  HTMLServer --|> SimpleHTTPRequestHandler
}

file "APIHandler"{
  class RequestHandler{
    self.path
    get_ext_from_folder()
    build_list_items()
    do_GET()
  }

  () "run()"

  RequestHandler --|> BaseHTTPRequestHandler
}

file "XMLExtractor" {
  () "build_items(root)"
  () "generate_class_diagram(path)"
  () "get_class_diagram(path)" 
}

file "plantUMLConnector"{
  class PlantUML{
    generate_svg(plantuml_code)
    generate_png(plantuml_code)
    generate_pdf(plantuml_code)
    generate_text(plantuml_code)
  }

  () "check_docker_container()"
}

folder "DataClasses"{
  file "attribute" {
    class Attribute{
      name
      type
      description
      puml_attrib_string
      __str__()
    }
  }
  file "item" {
    class Item{
      item
      itemname
      type
      attributes
      relations
      puml_class_string
      set_attributes()
      __Str__()
    }
  }
  file "itemClass"{
    class "Class"{
      item
      attributes
      set_extends()
    }
  }
  itemClass.Class --|> item.Item
  file "relation"{
    class Relation{
      parent
      child
      connection_string
      label
      __str__()
    }
  }
  file "extendsArrow"{
    class ExtendsArrow{
      parent
      child
    }
  }
  extendsArrow.ExtendsArrow --|> relation.Relation
  file "typeArrow"{
    class TypeArrow{
      parent
      child
    }
  }
  typeArrow.TypeArrow --|> relation.Relation
  file "typegroup" {
    class Typegroup{
      typegroup
      puml_group_string
      itemtypes
      iterate_items()
      __str__()
    }
  }
  file "itemtypes"{
    class Itemtypes{
      itemtypes
      typegroups
      iterate_items()
      iterate_typegroups()
      __str__()
    }
  }
  item.Item::attributes ..> attribute.Attribute:List of
  item.Item::relations ..> extendsArrow.ExtendsArrow:List of
  attribute.Attribute::type ..> typeArrow.TypeArrow:Is of type
}

@enduml
