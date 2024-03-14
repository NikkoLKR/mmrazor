# Copyright (c) OpenMMLab. All rights reserved.
from .byot_connector import BYOTConnector
from .convmodule_connector import ConvModuleConnector
from .crd_connector import CRDConnector
from .factor_transfer_connectors import Paraphraser, Translator
from .fbkd_connector import FBKDStudentConnector, FBKDTeacherConnector
from .mgd_connector import MGDConnector, MGD3DConnector, MGDSwinConnector
from .norm_connector import NormConnector
from .ofd_connector import OFDTeacherConnector
from .torch_connector import TorchFunctionalConnector, TorchNNConnector
from .feature_transfer_connector import PatchEmbed, PatchMerging, SwinFeatureProjector

__all__ = [
    'ConvModuleConnector', 'Translator', 'Paraphraser', 'BYOTConnector',
    'FBKDTeacherConnector', 'FBKDStudentConnector', 'TorchFunctionalConnector',
    'CRDConnector', 'TorchNNConnector', 'OFDTeacherConnector', 'MGDConnector',
    'NormConnector','PatchEmbed', 'PatchMerging', 'MGD3DConnector', 'SwinFeatureProjector',
    'MGDSwinConnector'
]
